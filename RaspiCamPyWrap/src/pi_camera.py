#!/usr/bin/python
'''
Created on Aug 22, 2013

@author: Brad
'''
from cam.raspicam import RaspiCam

if __name__ == '__main__':
    cam = RaspiCam()
    cam.take_pics()      