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
        
        
        
    
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()