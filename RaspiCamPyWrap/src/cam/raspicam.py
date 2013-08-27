'''
Created on Aug 22, 2013

@author: Brad
'''
from datetime import datetime
import time
import subprocess
from utils.config import Config

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
        
        # Exposure and Automatic White Balance
        self.ex  = 'auto'
        self.awb = 'auto'
        
        # EV level
        self.photo_ev = 0
        
        # Photo dimensions and rotation
        self.photo_width  = 640
        self.photo_height = 480
        self.photo_rotate = 0
        
        self.photo_interval = 60 # Interval between photos (seconds)
        
        self.photo_dir = 'today'
    
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
                filename = self.photo_dir + '/photo_' + self.current_timestamp() + '.jpg'
                self.set_pic_vars_from_config()
                
                # Change exposure if it is dark out.
                if  self.is_night_time():
                    self.ex = 'night'
                else:
                    self.ex = 'auto'
                    
                cmd = 'raspistill -o ' + filename \
                                       + ' -t 1000 ' \
                                       + ' -ex ' + self.ex \
                                       + ' -awb ' + self.awb \
                                       + ' -ev ' + str(self.photo_ev) \
                                       + ' -w ' + str(self.photo_width) \
                                       + ' -h ' + str(self.photo_height) \
                                       + ' -rot ' + str(self.photo_rotate)
                subprocess.call(cmd, shell=True)
                time.sleep(self.photo_interval)
        
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            # User quit
            print("\nGoodbye!")
    
    
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
        The time range is [0:23].
        Ex. 8:00 AM is 8 while 8:00 PM is 20.
        
        :param dawn:  Defaulted to 7:00 AM.
        :param dusk:  Defaulted to 8:00 PM.
        '''
        return_val = False
        
        now = time.localtime()
        if now.tm_hour >= dusk and now.tm_hour <= dawn:
            return_val = True
    
        return return_val 


