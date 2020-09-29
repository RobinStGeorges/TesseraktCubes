import os, sys
import serial
import time
import ast
import requests 


ser = serial.Serial('/dev/ttyUSB0', 115200, 8, 'N', 1, timeout=1)

while True:
   line = ser.readline()
   print (line)



                          

                 
                                   
          