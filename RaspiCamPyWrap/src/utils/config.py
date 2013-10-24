'''
Created on Aug 23, 2013

@author: Brad
'''
import ConfigParser
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
        self.read_config_file()
        
    
    def read_config_file(self):
        '''
        This method reads the config file associated with the system 
        they are on (Windows or Linux).
        '''
        try:
            self.set_config_file_path()
            self.config = ConfigParser.ConfigParser()
            self.config.read(self.config_file)
        except Exception as e:
            print(e)
            
            
    def set_config_file_path(self):
        '''
        Path seems to be different on Windows and Linux platforms.
        This method makes up for the differences.
        
        '''
        system = platform.system()
        if system == 'Linux':
            self.config_file = os.path.abspath('../src/picam.config')
        elif system == 'Windows':
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
                # Convert strings to integers or floats
                if val.isdigit():
                    new_val = ast.literal_eval(val)
                    return_val.append((key, new_val))
                # Get original string values
                else:
                    return_val.append((key, val))
        except ConfigParser.NoSectionError:
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
        except ConfigParser.NoSectionError:
            print('A NoSectionError has occurred.')
                
        return return_val
    
    
    
# For quick debug purposes only
if __name__ == '__main__':
    conf = Config()
   
    vals = conf.get_picture_vals()
    print(vals)
