#!/usr/bin/env python
# coding: utf-8
import os
import time
import signal
import sys
import RPi.GPIO as GPIO
import lcddriver
pin = 36 # The pin ID, edit here to change it
maxTMP = 50 # The maximum temperature in Celsius after which we trigger the fan
GPIO.setmode (GPIO.BOARD)
display=lcddriver.lcd()

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin,GPIO.OUT)
    GPIO.setwarnings(False)
    return()
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    print("temp is {0}".format(temp)) #Uncomment here for testing
    return temp
def fanON():
    setPin(True)
    return()
def fanOFF():
    setPin(False)
    return()
def getTEMP():
    CPU_temp = float(getCPUtemperature())

    if sys.argv[1] == "on":
        fanON()
        display.lcd_clear()
        display.lcd_display_string("    Fan Kapali    ",1)
    else:
        fanOFF()
        display.lcd_clear()
        display.lcd_display_string("     Fan Acik    ",1)

    return()
def setPin(mode): # A little redundant function but useful if you want to add logging
    GPIO.output(pin, mode)
    return()
try:
    setup()
    getTEMP()
    time. sleep(8) # Read the temperature every 5 sec, increase or decrease this limit if you want
except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt
	GPIO.cleanup()

