'''
Created on Aug 22, 2013

@author: Brad
'''
import unittest
from cam.raspicam import RaspiCam
from datetime import datetime


class Test(unittest.TestCase):


    def setUp(self):
        self.cam = RaspiCam()


    def tearDown(self):
        self.cam = None


    def test_current_timestamp(self):
        expected = str(datetime.now())
        actual = self.cam.current_timestamp()
        
        # For visual inspection of actual timestamp.
        print(actual)
        
        # Just check the Year-Month-Day
        self.assertEqual(expected[:10], actual[:10], 'Values should be equal')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()