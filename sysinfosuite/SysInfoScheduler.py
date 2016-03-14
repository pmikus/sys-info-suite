"""Module to gather information from local system from scheduled executed
commands"""

# Modules
import csv
import datetime
import threading
import sched
import logging
import os
import sys
import subprocess

# Module information
__author__ = "Peter Mikus"
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Peter Mikus"
__email__ = "pmikus@cisco.com"
__status__ = "Production"

# Logging settings
G_LOGGER = logging.getLogger(__name__)
G_LOGGER.setLevel(logging.NOTSET)
G_LOG_HANDLER = logging.StreamHandler()
G_LOG_FORMAT = logging.Formatter("%(asctime)s: %(name)s - %(threadName)s \
                                 %(levelname)s - %(message)s")
G_LOG_HANDLER.setFormatter(G_LOG_FORMAT)
G_LOGGER.addHandler(G_LOG_HANDLER)

class SysInfoScheduler(object):
    """Handles scheduling and executing subprocess in threads"""
    dynamic_all = ()

    def __init__(self):
        self.dynamic_thrd = ()
        self.lock = threading.Lock()

    def process_exec(self, cmd):
        """Executes the process"""
        exec_start = str(datetime.datetime.now())
        try:
            G_LOGGER.info('Running subprocess open: %s', cmd)
            proc_open = subprocess.Popen(cmd,
                                         shell=True,
                                         stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE,
                                         close_fds=True)
            child_stdout, child_stderr = proc_open.communicate()
            child_stat = proc_open.wait()

            with self.lock:
                G_LOGGER.debug('Acquired lock')
                self.dynamic_all += ((exec_start,
                                      cmd,
                                      child_stdout,
                                      child_stderr,
                                      child_stat,
                                      str(datetime.datetime.now())),)
        except OSError as ex_error:
            G_LOGGER.critical('Subprocess open exception: %s', ex_error)
            sys.exit(2)

    def add_internal_scheduler(self, sched_arr):
        """Add scheduler items from array"""
        for item in sched_arr:
            G_LOGGER.debug('Scheduling thread: %s', item[1])
            self.dynamic_thrd += (threading.Timer(item[0],
                                                  self.process_exec,
                                                  [item[1]]),)

    def add_external_scheduler(self, sched_file):
        """Add scheduler items from file"""
        try:
            with open(sched_file) as file:
                reader = csv.reader(file)
                for row in reader:
                    G_LOGGER.debug('Scheduling thread: %s', row[1])
                    self.dynamic_thrd += (threading.Timer(int(row[0]),
                                                          self.process_exec,
                                                          [row[1]]),)
                    # pylint: disable=W0703
        except Exception as ex_error:
            G_LOGGER.error('Error reading configuration file: %s', ex_error)

    def run_scheduler(self):
        """Starts scheduled threads and waits to join them"""
        G_LOGGER.info('Executing scheduled items')
        for thrd in self.dynamic_thrd:
            G_LOGGER.debug('Executing thread: %s', thrd.getName())
            thrd.setDaemon(True)
            thrd.start()

        main_thread = threading.currentThread()
        for thrd in threading.enumerate():
            if thrd is main_thread:
                continue
            thrd.join()
