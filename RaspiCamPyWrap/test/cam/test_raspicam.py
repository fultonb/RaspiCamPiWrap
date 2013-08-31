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
        self.mydusk = 0
        self.mydawn = 0


    def tearDown(self):
        self.cam = None
        self.mydusk = None
        self.mydawn = None



    def test_current_timestamp(self):
        expected = str(datetime.now())
        actual = self.cam.current_timestamp()
        
        # For visual inspection of actual timestamp.
        print(actual)
        
        # Just check the Year-Month-Day
        self.assertEqual(expected[:10], actual[:10], 'Values should be equal')
        

    def test_is_night_time_for_night(self):
        self.set_to_night_time()
        expected = True
        actual = self.cam.is_night_time(dusk=self.mydusk, dawn=self.mydawn)
        
        self.assertEqual(expected, actual, 'Values should be equal')
        
        
    def test_is_night_time_for_day(self):
        self.set_to_day_time()
        expected = False
        actual = self.cam.is_night_time(dusk=self.mydusk, dawn=self.mydawn)
        
        self.assertEqual(expected, actual, 'Values should be equal')


    def test_is_night_time_for_same_dusk_and_dawn(self):
        try:
            self.cam.is_night_time(dusk=12, dawn=12)
        except:
            self.assertRaises(ValueError)
       
        
    def test_set_ex_and_awb_for_same_dusk_and_dawn(self):
        try:
            self.cam.dawn = 12
            self.cam.dusk = 12
            self.cam.set_ex_and_awb()
        except:
            self.assertRaises(ValueError)
            
            
    def test_set_ex_and_awb(self):
        night = 'NIGHT'
        day = 'DAY'        
        
        if(self.cam.is_night_time()):
            expected = night
            self.cam.photo_night_ex = night
            self.cam.photo_night_awb = night
        else:
            expected = day
            self.cam.photo_day_ex = day
            self.cam.photo_day_awb = day
            
        self.cam.set_ex_and_awb()
        
        actual_ex = self.cam.photo_ex
        actual_awb = self.cam.photo_awb
         
        self.assertEqual(expected, actual_ex, 'Values should be equal')
        self.assertEqual(expected, actual_awb, 'Values should be equal')
        
    
    def test_set_self_vars_from_config_VISUALLY(self):        
        '''
        Since these values can be changed at any time, you can visually read
        the src/picam.config file and compare it to this output.
        '''
        self.cam.set_pic_vars_from_config()
        print(vars(self.cam))


    def test_create_photo_filename_VISUALLY(self):
        '''
        The filename uses the current date, so this will be inspected visually.
        '''
        self.cam.set_pic_vars_from_config()
        filename = self.cam.create_photo_filename()
        print(filename)


    #----------------------- Helper functions --------------------------------#
    
    def set_to_night_time(self):
        '''
        To simulate night time, place the hours of dawn and dusk 
        around the current time.
        '''
        now = time.localtime()
        the_hour = now.tm_hour
        print(the_hour)
        if the_hour == 23:
            self.mydusk = 22
            self.mydawn = 2
        elif the_hour == 0:
            self.mydusk = 22
            self.mydawn = 2
        else:
            self.mydusk = the_hour - 1
            self.mydawn = the_hour + 1
        
        
    def set_to_day_time(self):
        '''
        To simulate day time, place the hours of dawn and dusk 
        after the current time.
        '''
        now = time.localtime() 
        the_hour = now.tm_hour
        
        if the_hour >= 22:
            self.mydusk = 1
            self.mydawn = 2
        else:
            self.mydusk = the_hour + 1
            self.mydawn = the_hour + 2     
        
   
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()