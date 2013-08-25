'''
Created on Aug 23, 2013

@author: Brad
'''
import configparser
import os

class Config(object):
    '''
    This class reads a config file and returns its values.
    '''

    config_file = os.path.abspath('../../src/picam.config')

    def __init__(self):
        '''
        Constructor
        '''
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)
        
        
    def get_picture_vals(self):
        '''
        Returns an array of tuples holding the key/value pairs.
        Ex.  [('ex', 'auto'), ('awb', 'auto'), ('photo_ev', '0'), ...]

        '''
        return self.config.items('pictures')
        
                
    def get_video_vals(self):
        '''
        Returns an array of tuples holding the key/value pairs.
        Ex.  [('ex', 'auto'), ('awb', 'auto'), ('photo_ev', '0'), ...]

        '''
        return self.config.items('video')
                
                
    def get_sections(self): 
        '''
        Returns a list of the sections contained in the config file.
        Ex.  ['pictures', 'video']
        '''
        return self.config.sections()
    
    
    def get_keys(self, section):
        '''
        Returns a list of key values from the config file.
        Ex. ['ex', 'awb', 'photo_ev', 'photo_width', 'photo_height', ...]
                
        :param section:  'pictures' or 'video'
        '''
        
        return [key for key in self.config[section]]
    
    
    
if __name__ == '__main__':
    conf = Config()
   
    print(conf.get_keys('pictures'))
    vals = conf.get_picture_vals()
    print(vals)
#     for (key, val) in vals:
#         print(key + ' : ' + val)