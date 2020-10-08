#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
import sys
import lcddriver

display= lcddriver.lcd()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)
pwm=GPIO.PWM(10, 50)
pwm.start(0)

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(10, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(10, False)
	pwm.ChangeDutyCycle(0)
if sys.argv[1] == "on":
   SetAngle(175) 
   display.lcd_clear()
   display.lcd_display_string("    Kapi Acik    ",1)
   sleep(2)
else:
   display.lcd_clear()
   display.lcd_display_string("    Kapi Kapali    ",1)
   sleep(2)
   SetAngle(110)

pwm.stop()
GPIO.cleanup()
