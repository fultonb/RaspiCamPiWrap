'''
Created on Aug 23, 2013

@author: Brad
'''
import configparser
import os
import platform
import ast


#===============================================================================
# Config
#
# This class reads a config file and returns its values.
#
# The config file used is src/picam.config
#
#===============================================================================
class Config(object):
    '''
    This class reads a config file and returns its values.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.set_config_file_path()
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)
        
        
    def set_config_file_path(self):
        # Default
        self.config_file = os.path.abspath('../src/picam.config')
        
        system = platform.system()
        if system is 'Linux':
            self.config_file = os.path.abspath('../src/picam.config')
        elif system is 'Windows':
            self.config_file = os.path.abspath('../../src/picam.config')
        
        
    def get_picture_vals(self):
        '''
        Returns an array of tuples holding the key/value pairs for all values 
        in the [picture] section of the config file.
        Ex.  [('ex', 'auto'), ('awb', 'auto'), ('photo_ev', '0'), ...]

        '''
        return_val = []
        try:
            items = self.config.items('pictures')
            for (key, val) in items:
                # Get original string values
                if val.isalpha():
                    return_val.append((key, val))
                # Convert strings to integers or floats
                elif val.isdigit():
                    new_val = ast.literal_eval(val)
                    return_val.append((key, new_val))
        except configparser.NoSectionError:
            print('A NoSectionError has occurred.')
                
        return return_val
        
                
    def get_video_vals(self):
        '''
        Returns an array of tuples holding the key/value pairs.
        Ex.  [('ex', 'auto'), ('awb', 'auto'), ('photo_ev', '0'), ...]

        '''
        return_val = []
        try:
            return_val = self.config.items('video')
        except configparser.NoSectionError:
            print('A NoSectionError has occurred.')
                
        return return_val
    
    
    
# For quick debug purposes only
if __name__ == '__main__':
    conf = Config()
   
    vals = conf.get_picture_vals()
    print(vals)
