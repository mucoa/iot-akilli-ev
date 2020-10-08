#!/usr/bin/python

import sys
#from pyfirmata import Arduino, util
import time
import lcddriver
import RPi.GPIO as GPIO
import subprocess


# kontrol func
def ctrl(pin, mode): 
	if mode == "on":		
   	 GPIO.output(pin,GPIO.HIGH)
	 time.sleep(2)
	 display.lcd_clear()
	 display.lcd_display_string("    isik acik   ",1)
	 time.sleep(2)
	elif mode == "off": 
	 GPIO.output(pin,GPIO.LOW)
	 time.sleep(2)
	 display.lcd_clear()
	 display.lcd_display_string("   isik kapali   ",1)
	 time.sleep(2)
	else: 
	 print("-----------------------\non yada off olarak sadece 1 parametre almalidir")
	return quit()
# arduino board
#board = Arduino('/dev/ttyUSB0')
#pin = arduino_start.board.digital

display = lcddriver.lcd()

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setwarnings(False)
GPIO.setup(37, GPIO.OUT)

# parametreler ayarlaniyor
if len(sys.argv) != 2:
	funcm="nan"
elif sys.argv[1] == "on" or sys.argv[1] == "off":
	funcm=sys.argv[1]
else:
	funcm="nan"

ctrl(37, funcm)
GPIO.cleanup()
