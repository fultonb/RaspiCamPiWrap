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
        
    
    def test_get_log_vals_VISUALLY(self):        
        '''
        Since these values can be changed at any time, you can visually read
        the src/picam.config file and compare it to this output.
        '''
        print(self.conf.get_log_vals())
     
         
    def test_get_logging_vals(self):        
        '''
        Since these values can be changed at any time, you can visually read
        the src/picam.config file and compare it to this output.
        '''
        self.log_dir = 'some_phony_value'
        actual_value = '../log/'
        
        log_vals = self.conf.get_log_vals()
        for (key, val) in log_vals:
            setattr(self, key, val)
            
        self.assertEqual(self.log_dir, actual_value, 'Should be the same values.')
    
    
    def test_NameError_in_get_vals(self):
        '''
        If a value other than pictures, video, or logging is used 
        in __get_vals(), a NameError Exception should be thrown.
        '''
        error_raised = False
        try:
            # Note: you must use this syntax to access a private function.
            self.conf._Config__get_vals('some_bad_value')
        except NameError as ne:
            error_raised = True
            self.assertEqual(True, error_raised, 'NameError should have been raised.')
            print(ne)
            return
            
        self.assertFalse(error_raised, 'Should NOT get here.')


    def test_for_NO_NameError_in_get_vals(self):
        '''
        If a value other than pictures, video, or logging is used 
        in __get_vals(), a NameError Exception should be thrown.
        '''
        error_raised = False
        try:
            # Note: you must use this syntax to access a private function.
            self.conf._Config__get_vals('pictures')
            self.conf._Config__get_vals('video')
            self.conf._Config__get_vals('logging')
        except NameError as ne:
            error_raised = True
            self.assertEqual(True, error_raised, 'Should NOT get here.')
            print(ne)
            return
            
        self.assertFalse(error_raised, 'NameError should NOT have been raised.')




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()