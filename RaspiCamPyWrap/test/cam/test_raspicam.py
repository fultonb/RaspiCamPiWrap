'''
Created on Aug 22, 2013

@author: Brad
'''
import unittest
from cam.raspicam import RaspiCam
from datetime import datetime
import time


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
        
        
    def test_is_night_time(self):
        now = time.localtime()
        expected = False
        if now.tm_hour >= 20 and now.tm_hour <= 7:
            expected = True
        actual = self.cam.is_night_time()
        
        # For visual inspection of actual time.
        print(now)
        
        # Just check the Year-Month-Day
        self.assertEqual(expected, actual, 'Values should be equal')
        

    def test_is_night_time_for_night(self):
        # To simulate night time, place the hours of dawn and dusk 
        # around the current time.
        now = time.localtime()
        mydusk = now.tm_hour - 1
        mydawn = now.tm_hour + 1
        expected = True
        actual = self.cam.is_night_time(dusk=mydusk, dawn=mydawn)
        
        # Just check the Year-Month-Day
        self.assertEqual(expected, actual, 'Values should be equal')
        
        
    def test_is_night_time_for_day(self):
        # To simulate day time, place the hours of dawn and dusk 
        # after the current time.
        now = time.localtime()
        mydusk = now.tm_hour + 1
        mydawn = now.tm_hour + 2
        expected = False
        actual = self.cam.is_night_time(dusk=mydusk, dawn=mydawn)
        
        # Just check the Year-Month-Day
        self.assertEqual(expected, actual, 'Values should be equal')





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()