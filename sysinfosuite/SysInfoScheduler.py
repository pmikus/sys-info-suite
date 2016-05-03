"""Module to gather information from local system from scheduled executed
commands"""

import csv
import datetime
import logging
import sys
import subprocess
import threading

# Module information
__author__ = "Peter Mikus"
__license__ = "GPLv3"
__version__ = "2.1.0"
__maintainer__ = "Peter Mikus"
__email__ = "pmikus@cisco.com"
__status__ = "Production"

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

class SysInfoScheduler(object):
    """Handles scheduling and executing subprocess in threads."""
    dynamic_all = ()

    def __init__(self):
        self.dynamic_thrd = ()
        self.lock = threading.Lock()

    def process_exec(self, cmd):
        """Executes the process.

        :param cmd: command to run
        :type cmd: string
        :return: nothing
        """

        exec_start = str(datetime.datetime.now())
        try:
            LOGGER.info('Running subprocess open: {}'.format(cmd))
            proc_open = subprocess.Popen(cmd,
                                         shell=True,
                                         stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE,
                                         close_fds=True)
            child_stdout, child_stderr = proc_open.communicate()
            child_stat = proc_open.wait()

            with self.lock:
                LOGGER.debug('Acquired lock')
                self.dynamic_all += ((exec_start,
                                      cmd,
                                      child_stdout,
                                      child_stderr,
                                      child_stat,
                                      str(datetime.datetime.now())),)
        except OSError as ex_error:
            LOGGER.exception('Subprocess open exception: {}'.format(ex_error))
            sys.exit(2)

    def add_internal_scheduler(self, sched_arr):
        """Add scheduler items from array.

        :param sched_arr: array with sheduling information
        :type sched_arr: array
        :return: nothing
        """
        for item in sched_arr:
            LOGGER.debug('Scheduling thread: {}'.format(item[1]))
            self.dynamic_thrd += (threading.Timer(item[0],
                                                  self.process_exec,
                                                  [item[1]]),)

    def add_external_scheduler(self, sched_file):
        """Add scheduler items from file.

        :param sched_file: file with sheduling information
        :type sched_file: string
        :return: nothing
        """
        try:
            with open(sched_file) as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    LOGGER.debug('Scheduling thread: {}'.format(row[1]))
                    self.dynamic_thrd += (threading.Timer(int(row[0]),
                                                          self.process_exec,
                                                          [row[1]]),)
                    # pylint: disable=W0703
        except Exception as ex_error:
            LOGGER.exception('Error reading configuration file: {}'.format(
                ex_error))

    def run_scheduler(self):
        """Starts scheduled threads and waits to join them.

        :return: nothing
        """
        LOGGER.info('Executing scheduled items')
        for thrd in self.dynamic_thrd:
            LOGGER.debug('Executing thread: {}'.format(thrd.getName()))
            thrd.setDaemon(True)
            thrd.start()

        main_thread = threading.currentThread()
        for thrd in threading.enumerate():
            if thrd is main_thread:
                continue
            thrd.join()
