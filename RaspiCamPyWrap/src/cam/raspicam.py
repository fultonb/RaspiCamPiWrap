'''
Created on Aug 22, 2013

@author: Brad
'''
from datetime import datetime
import time
from time import strftime
import subprocess
from utils.config import Config
import os



#===============================================================================
# RaspiCam
#
#  This class is the camera class which manages all camera operations on the
#  RaspberryPi.  It does the following:
#    1.  Take a photo at any time interval you set.  Default is every minute.
#    2.  Every photo will be given a name including a time stamp of when the 
#        photo was taken.
#
#===============================================================================
class RaspiCam(object):

    def __init__(self):
        '''
        Constructor
        
        See src/picam.config file for all options.
        More documentation at:
        http://www.raspberrypi.org/wp-content/uploads/2013/07/RaspiCam-Documentation.pdf
        
        These default values can be changed or added to, in the picam.config file.
        '''
        # Default values:
        
        # Exposure
        self.photo_ex  = None        
        self.photo_day_ex = 'auto'
        self.photo_night_ex = 'auto'
        
        # Automatic White Balance
        self.photo_awb = None
        self.photo_day_awb = 'auto'
        self.photo_night_awb = 'auto'
        
        # EV level
        self.photo_ev = 0
        
        # Photo dimensions and rotation
        self.photo_width  = 640
        self.photo_height = 480
        self.photo_rotate = 0
        
        self.photo_interval = 60 # Interval between photos (seconds)
        
        self.photo_dir = 'pics'
        self.photo_name = 'photo'
        
        self.dawn = 7
        self.dusk = 20
    
        # Config object used to get values from the config file.
        self.conf = Config()
        
    
    def set_pic_vars_from_config(self):
        '''
        This method will set attributes for pictures, from:
           src/picam.config
           
        If the config file does NOT exist, then the default values in the 
        constructor will be used.
        '''        
        pic_vals = self.conf.get_picture_vals()
        for (key, val) in pic_vals:
            setattr(self, key, val)
     
        
    def take_pics(self):
        '''
        This method uses the linux raspistill application to take pictures.
        At night, the exposure is set to 'night'.
        Pictures are taken every minute (default).  This time can be changed in
        the picam.config file.
        '''
        # Lets start taking photos!
        try:                    
            while True:
                self.set_pic_vars_from_config()
                filename = self.create_photo_filename()                
                
                # Set Exposure and Automatic White Balance for day or night time.
                self.set_ex_and_awb()
                
                # This command takes a single picture.
                cmd = 'raspistill -o ' + filename \
                                       + ' -t 1000 ' \
                                       + ' -ex ' + self.photo_ex \
                                       + ' -awb ' + self.photo_awb \
                                       + ' -ev ' + str(self.photo_ev) \
                                       + ' -w ' + str(self.photo_width) \
                                       + ' -h ' + str(self.photo_height) \
                                       + ' -rot ' + str(self.photo_rotate)
                subprocess.call(cmd, shell=True)
                
                # Sleep until it is time for the next picture.
                time.sleep(self.photo_interval)
        
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            # User quit
            print("\nGoodbye!")
    
    
    def create_photo_filename(self):
        '''
        This method will create a base directory using the photo_dir config 
        variable.
        A sub directory will be created in the format of Year_Month_Day.
        The filename consists of the 'name' argument passed into the method 
        and a timestamp.
        
        Ex. ./pics/2013_08_30/photo_2013-08-30_09-59-09.501599.jpg
        '''
        # Create directory if it doesn't already exist.
        directory = self.photo_dir + '/' + strftime('%Y_%m_%d')
        self.create_dir(directory)
        
        filename = directory + '/' + self.photo_name + '_' + self.current_timestamp() + '.jpg'
        
        return filename
        
        
    def create_dir(self, directory):
        '''
        This method will create a directory if it doesn't already exist.
        '''
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except Exception as e:
            print(e)
            
            
    def set_ex_and_awb(self):
        '''
        This method changes the Exposure and Automatic White Balance for
        day or night time.
        '''
        try:
            if self.is_night_time(dawn=self.dawn, dusk=self.dusk):
                self.photo_ex = self.photo_night_ex
                self.photo_awb = self.photo_night_awb
            else:
                self.photo_ex = self.photo_day_ex
                self.photo_awb = self.photo_day_awb      
        except ValueError as ve:
            print(ve + ' Default values will be used.')              
        
        
    def current_timestamp(self):
        '''
        Returns a timestamp in the following format:
            year-month-day_hour-min-sec
            2013-08-25_09-31-59.126116
        '''
        # Remove spaces and colons.
        now = str(datetime.now()).replace(' ', '_')
        return now.replace(':', '-')

        
    def is_night_time(self, dawn=7, dusk=20):
        '''
        Returns True if night time else False.
        Night time is considered to be the hours between dawn and dusk. 
        We are making the assumption that dusk or dawn are never the same.
        
        The time range is [0:23].
        Ex. 8:00 AM is 8 while 8:00 PM is 20.
        
        :param dawn:  Defaulted to 7:00 AM.
        :param dusk:  Defaulted to 8:00 PM.
        '''
        # dawn and dusk cannot be the same value.
        if dawn == dusk:
            raise ValueError('dawn and dusk cannot be the same value')
        
        is_night = True        
        now = time.localtime()
        the_hour = now.tm_hour
            
        # Day time is when the_hour is NOT between dusk and dawn.
        
        # dusk before midnight and dawn after midnight
        if (dusk <= 23 and dusk >= 12) and (dawn >= 0 and dawn <= 12):
            if the_hour < dusk and the_hour > dawn:
                is_night = False
        
        # dusk before midnight and dawn before midnight
        elif (dusk <= 23 and dusk >= 12) and (dawn <= 23 and dawn >= 12):
            if the_hour < dusk:
                is_night = False
        
        # dusk after midnight and dawn after midnight
        elif (dusk >= 0 and dusk <= 12) and (dawn >= 0 and dawn <= 12):
            if the_hour < dusk:
                is_night = False
    
        return is_night 


