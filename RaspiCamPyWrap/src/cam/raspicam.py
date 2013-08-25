'''
Created on Aug 22, 2013

@author: Brad
'''
from datetime import datetime
import time
import subprocess


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
        '''
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
    
    
    def take_pics(self):
        # Lets start taking photos!
        try:
            while True:
                filename = self.photo_dir + '/photo_' + self.current_timestamp() + '.jpg'
                
                if  self.is_night_time():
                    self.ex = 'night'
                else:
                    self.ex = 'auto'
                    
                cmd = 'raspistill -o ' + filename \
                                       + ' -t 1000 -ex ' + self.ex \
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
        # Remove spaces and colons.
        now = str(datetime.now()).replace(' ', '_')
        return now.replace(':', '-')
    
    
    def is_night_time(self):
        returnVal = False
        
        now = time.localtime()
        if now.tm_hour >= 20 and now.tm_hour <= 7:
            returnVal = True
    
        return returnVal 


