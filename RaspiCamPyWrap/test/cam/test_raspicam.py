'''
Created on Aug 22, 2013

@author: Brad
'''
import unittest
from cam.raspicam import RaspiCam


class Test(unittest.TestCase):


    def setUp(self):
        self.cam = RaspiCam()


    def tearDown(self):
        self.cam = None


    def test_current_timestamp(self):
        expected = '2013-08-25_09-31-59.126116'
        actual = self.cam.current_timestamp()
        
        self.assertEqual(expected, actual, 'Values should be equal')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()