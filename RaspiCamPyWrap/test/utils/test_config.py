'''
Created on Aug 23, 2013

@author: Brad
'''
import unittest
from utils.config import Config


class Test(unittest.TestCase):

    conf = None
    
    def setUp(self):
        self.conf = Config()


    def tearDown(self):
        self.conf = None
        

    def test_get_picture_vals_VISUALLY(self):        
        '''
        Since these values can be changed at any time, you can visually read
        the src/picam.config file and compare it to this output.
        '''
        print(self.conf.get_picture_vals())
        
        
    def test_get_logging_vals_VISUALLY(self):        
        '''
        Since these values can be changed at any time, you can visually read
        the src/picam.config file and compare it to this output.
        '''
        self.log_dir = 'some_phony_value'
        log_vals = self.conf.get_log_vals()
        for (key, val) in log_vals:
            setattr(self, key, val)
            
        print self.log_dir
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()