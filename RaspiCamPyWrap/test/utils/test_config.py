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
        

    def test_get_sections(self):        
        expected = ['pictures', 'video']
        actual = self.conf.get_sections()
        
        self.assertEqual(expected, actual, 'Values should be equal')
        
        
    def test_get_picture_keys(self):
        expected = ['ex', 'awb', 'photo_ev', 'photo_width', 'photo_height', 
                    'photo_rotate', 'photo_interval', 'photo_dir']
        
        actual = self.conf.get_keys('pictures')
        
        self.assertEqual(expected, actual, 'Values should be equal')
        
        
    def test_get_video_keys(self):
        expected = []
        actual = self.conf.get_keys('video')
        
        self.assertEqual(expected, actual, 'Values should be equal')
    
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()