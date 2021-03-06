#######################################################################
#  Name:                 Oxygen Sensor Wireless
#  File Name:            oxygen_sensor.c    (To Be Defined)
#  Start Date:           22/October/2018
#  Developed by:         ShrikeLab
#  Programmer:           Andres Garcia Rubio
#  Experiment:           Algae
#  References:           Github link:
#  Language:             Python
#  Abstract:             Script for oxygen sensor using protocol TCP/IP
#  Hardware:             Raspberry Pi Zero W
#  IDE:                  Sublime Text
#######################################################################

import serial
import time
import csv
from gpiozero import LED
import RPi.GPIO as GPIO

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


#hardware constants declarations
green = LED(27)
red = LED(22)
toggleSwitch = 12

#serial bus declaration
serial_handler = serial.Serial('/dev/ttyS0',9600,timeout=0)

#Settings for GPIO and serial bus
GPIO.setmode(GPIO.BCM)
GPIO.setup(toggleSwitch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

samples_taken = 0
samples_goal = 30

buffer_time = 0.5


def main():
    try:
      time.sleep(buffer_time)
      ser_bytes = serial_handler.readline()
      if(GPIO.input(toggleSwitch)):
        with open("/var/www/html/oxygendata.csv","a") as f:
          if(ser_bytes!=''):
            writer = csv.writer(f,delimiter=",")
            writer.writerow([time.time(),time.strftime("%a %d-%m-%Y @ %H:%M:%S"),ser_bytes])
            green.on()
            samples_taken = samples_taken + 1
          if(samples_takenples == samples_goal):
            red.on()
      else:
         samples_taken = 0
         print("off")
         green.off()
         red.off()
    except:
      print("keyboard int")        

while(True):
    main()

