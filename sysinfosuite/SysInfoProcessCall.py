"""Module handles sub-processes/SSH/HTTP calls"""

import logging
import socket
import subprocess
import sys
import xml.etree.ElementTree as ET
try:
    import paramiko
except ImportError:
    sys.stderr.write('Paramiko library is required to run the script.\n' \
                     'To install the library run the following command:\n' \
                     '\tUbuntu/Debian: apt-get install python-paramiko\n' \
                     '\tFedora/RHEL/CentOS: yum install python-paramiko\n')
    sys.exit(2)

__author__ = "Peter Mikus"
__license__ = "GPLv3"
__version__ = "2.1.0"
__maintainer__ = "Peter Mikus"
__email__ = "pmikus@cisco.com"
__status__ = "Production"

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

class SysInfoProcessCall(object):
    """Handles sub-processes/SSH/HTTP calls."""

    # pylint: disable=R0902
    def __init__(self, host='', username='', password='', keyfile=''):
        self.child_stdout = ''
        self.child_status = 0
        self.child_stderr = ''
        self.ssh = ''
        self.host = host
        self.username = username
        self.password = password
        self.keyfile = keyfile

    def get_process_stdout(self):
        """Returns output from stdout.

        :return: output from stdout
        :rtype: string
        """
        return self.child_stdout

    def get_process_stderr(self):
        """Returns output from stderr.

        :return: output from stderr
        :rtype: string
        """
        return self.child_stderr

    def get_process_status(self):
        """Returns status of the command call.

        :return: return code of process
        :rtype: string
        """
        return self.child_status

    def get_process_output(self):
        """Returns output from stdout or stderr.

        :return: output from stdout or stderr based status
        :rtype: string
        """
        if not self.child_status:
            return self.child_stdout
        else:
            return self.child_stderr

    def execute_process_locally(self, cmd, cmd_input=''):
        """Create subprocess and run the command.

        :param cmd: command to run
        :param cmd_input: input to command
        :type cmd: string
        :type cmd_input: string
        :return: nothing
        """
        try:
            LOGGER.info('Running command on local host (subprocess)')
            LOGGER.info('Command to run: {}'.format(cmd))
            proc_open = subprocess.Popen(cmd,
                                         shell=True,
                                         stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE,
                                         close_fds=True)
            self.child_stdout, self.child_stderr = proc_open.communicate(\
                        cmd_input)
            self.child_status = proc_open.wait()
        except OSError as ex_error:
            self.child_status = 255
            LOGGER.exception('Subprocess open exception: {}'.format(ex_error))

    # pylint: disable=R0913
    def execute_process_remotely(self, cmd, host, username, password, keyfile):
        """Create SSH session and run the command.

        :param cmd: command to run
        :param host: remote host
        :param username: username
        :param password: password
        :param keyfile: keyfile
        :type cmd: string
        :type host: string
        :type username: string
        :type password: string
        :type keyfile: string
        :return: nothing
        """
        try:
            LOGGER.info('Creating SSH session to host: {}'.format(host))
            if not self.ssh:
                self.ssh = paramiko.SSHClient()
                self.ssh.set_missing_host_key_policy(\
                        paramiko.AutoAddPolicy())
                self.ssh.connect(host, username=username, password=password,
                                 key_filename=keyfile)
            LOGGER.info('Command to run over SSH: {}'.format(cmd))
            tmp_stdin, tmp_stdout, tmp_stderr = self.ssh.exec_command(cmd)
            tmp_stdin.close()
            self.child_stdout = tmp_stdout.read()
            self.child_stderr = tmp_stderr.read()
            self.child_status = tmp_stdout.channel.recv_exit_status()
        except paramiko.AuthenticationException as ex_error:
            self.ssh.close()
            self.ssh = ''
            self.child_status = 255
            LOGGER.exception('SSH to device {}: {}'.format(self.host,
                                                           ex_error))
        except socket.error as ex_error:
            self.ssh.close()
            self.ssh = ''
            self.child_status = 255
            LOGGER.exception('SSH to device {}: {}'.format(self.host,
                                                           ex_error))

    def execute_process(self, cmd, cmd_input=''):
        """Execute command locally or over SSH session.

        :param cmd: command to run
        :param cmd_input: input to command
        :type cmd: string
        :type cmd_input: string
        :return: nothing
        """
        if not self.host:
            self.execute_process_locally(cmd, cmd_input)
        else:
            self.execute_process_remotely(cmd, self.host, self.username,
                                          self.password, self.keyfile)

    def get_bios_from_ucs240(self, classid):
        """Create subprocess and run the command"""
        try:
            LOGGER.info('Running command on local host (subprocess)')
            cmd = "curl -s -3 -k -X POST --data '<aaaLogin \
                   inName=\""+self.username+"\" \
                   inPassword=\""+self.password+"\" />' \
                   https://"+self.host+"/nuova"

            LOGGER.info('Command to run: {}'.format(cmd))
            self.execute_process_locally(cmd)

            if not self.child_status:
                ccc = ET.fromstring(self.child_stdout).attrib.get('outCookie')
                if ccc:
                    LOGGER.info('Connected to CIMC host: {}, \
                                [Cookie: {}]'.format(self.host, ccc))
                    cmd = "curl -s -3 -k -X POST --data '<configResolveClass \
                           cookie=\""+ccc+"\" \
                           inHierarchical=\"true\" \
                           classId=\""+classid+"\" />' \
                           https://"+self.host+"/nuova"

                    LOGGER.info('Command to run: {}'.format(cmd))
                    self.execute_process_locally(cmd)

                    cmd = "curl -s -3 -k -X POST --data '<aaaLogout \
                           inCookie=\""+ccc+"\" />' \
                           https://"+self.host+"/nuova"

                    LOGGER.info('Loging out from CIMC of host: {}, \
                                [Cookie: {}]'.format(self.host, ccc))
                    _ = subprocess.Popen(cmd,
                                         shell=True,
                                         stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE,
                                         close_fds=True)
                else:
                    LOGGER.critical('Failed to get cookie from CIMC')
            else:
                LOGGER.critical('Failed to get data from CIMC: {}'.format(
                    self.child_stderr))
        except OSError as ex_error:
            self.child_status = 255
            LOGGER.exception('Subprocess open exception: {}'.format(ex_error))
