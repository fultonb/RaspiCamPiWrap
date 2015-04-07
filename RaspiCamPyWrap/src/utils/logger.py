'''
Created on Aug 23, 2013

@author: Brad
'''
import logging.handlers
import os

class Logger(object):
    '''
    This is a wrapper class for logging.
    
    Levels        When it is used
    ------        ---------------
    DEBUG         Detailed information, typically of interest only when 
                  diagnosing problems.
    INFO          Confirmation that things are working as expected.
    WARNING       An indication that something unexpected happened, 
                  or indicative of some problem in the near future 
                  (e.g. 'disk space low'). The software is still 
                  working as expected.
    ERROR         Due to a more serious problem, the software has not 
                  been able to perform some function.
    CRITICAL      A serious error, indicating that the program itself 
                  may be unable to continue running.
    
    '''

    def __init__(self):
        '''
        Constructor
        '''
        # Default values.
        self.LOG_DIR = './log/'
        self.LOG_FILENAME = 'logging_rotatingfile_example.out'
        self.level = logging.DEBUG
        self.maxBytes = 1000000
        self.backupCount = 4
        
        
    def createLogger(self, name='MyLogger'):
        '''
        This method creates a logger using the default values.
        
        Change default values before calling this method if you need 
        something different, such as a different logging directory.
        
        Ex. 
            log = Logger()
            log.LOG_DIR = '/tmp/'
            log.createLogger(name='TestLogger')
        '''
        
        self.setLogDirAndName()
        
        # Set up a specific logger with our desired output level.
        my_logger = logging.getLogger(name)
        my_logger.setLevel(self.level)
        
        # Create file handler which logs even debug messages.
        handler = logging.handlers.RotatingFileHandler(
                    self.LOG_DIR_AND_NAME, maxBytes=self.maxBytes, backupCount=self.backupCount)
        
        # Create formatter. 
        # 2015-04-04 17:29:25,465 - 
        # DEBUG - 
        # /Users/bradfulton/GitRepos/RaspiCamPiWrap/RaspiCamPyWrap/test/utils/test_logger.py - 
        # test_format_VISUALLY - 
        # 66 - 
        # debug message
        my_format = '%(asctime)s - %(levelname)s - %(pathname)s - %(funcName)s - %(lineno)d - %(message)s'
        formatter = logging.Formatter(my_format)
        # And add it to the handler.
        handler.setFormatter(formatter)
        
        # Add the log message handler to the logger.
        my_logger.addHandler(handler)
        
        return my_logger
    
    
    def setLogDirAndName(self):
        '''
        This method creates the logging directory if needed and sets 
        the LOG_DIR_AND_NAME variable using the directory and file names.
        '''
        self.createLogDir()
        self.LOG_DIR_AND_NAME = self.LOG_DIR + self.LOG_FILENAME
        
        
    def createLogDir(self):
        '''
        This method creates the logging directory if it doesn't already exist.
        If the directory cannot be created, then a local log directory will be
        created.
        '''
        directory = self.LOG_DIR
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except Exception:
            print 'Could not create: ' + os.path.realpath(self.LOG_DIR)
            self.createDefaultLogDir()
            
            
    def createDefaultLogDir(self):
        '''
        This method creates the default logging directory (./log/).
        '''
        self.LOG_DIR = './log/'
        directory = self.LOG_DIR
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
                
            print 'Created: ' + os.path.realpath(self.LOG_DIR)
        except Exception as e:
            print e
                   
