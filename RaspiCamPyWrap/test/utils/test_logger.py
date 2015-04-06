'''
Created on Apr 4, 2015

@author: bradfulton
'''
import unittest
import glob
import os
import logging
from utils.logger import Logger


class Test(unittest.TestCase):
    
    def setUp(self):
        self.my_log = Logger()


    def tearDown(self):
        self.my_log = None
        

    def test_get_logs_VISUALLY(self):        
        '''
        Creates and prints the following files:
            /tmp/my_test_rotatingfile_example.out
            /tmp/my_test_rotatingfile_example.out.1
            /tmp/my_test_rotatingfile_example.out.2
            /tmp/my_test_rotatingfile_example.out.3
            /tmp/my_test_rotatingfile_example.out.4
            /tmp/my_test_rotatingfile_example.out.5
            
        Then deletes them.
        '''
        # Create test logger.
        self.my_log.LOG_DIR = '/tmp/'
        self.my_log.LOG_FILENAME = 'my_test_rotatingfile_example.out'
        self.my_log.level=logging.DEBUG
        self.my_log.maxBytes = 20
        self.my_log.backupCount = 5
        log = self.my_log.createLogger(name='TestLogger')
        
        # Log some messages.
        for i in range(20):
            log.debug('i = %d' % i)
        
        # See what files are created.
        logfiles = glob.glob('%s*' % self.my_log.LOG_DIR_AND_NAME)
        
        for filename in logfiles:
            print(filename)
        
        # Clean up.
        for filename in logfiles:
            os.remove(filename)
            
            
    def test_format_VISUALLY(self):
        """
        Writes messages to a log file.
        Prints out messages in the log file.
        Deletes the log file.
        """
        # Create default test logger.
        self.my_log.LOG_DIR = '/tmp/'
        log = self.my_log.createLogger(name='MyTestLogger')
        
        log.debug('debug message')
        log.info('info message')
        log.warn('warn message')
        log.error('error message')
        log.critical('critical message')
        
        workfile = self.my_log.LOG_DIR_AND_NAME
        with open(workfile, 'r') as f:
            for line in f:
                print line,

        # See what files are created.
        logfiles = glob.glob('%s*' % self.my_log.LOG_DIR_AND_NAME)
        
        # Clean up.
        for filename in logfiles:
            os.remove(filename)
            
            
            
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()