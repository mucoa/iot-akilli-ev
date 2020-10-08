#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import lcddriver
import arduino_start
import subprocess

#subprocess.call(["sudo", "systemctl", "stop", "smart-lights"])

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

display=lcddriver.lcd()
display.lcd_clear()
display.lcd_display_string("   Garaj Acik   ", 1)
time.sleep(3)

TRIG = 23
ECHO = 24
DELAY=1
ACIK= 150
KAPA= 40

servo = arduino_start.board.get_pin('d:9:s')


def move_servo(v):
    servo.write(v)
    arduino_start.board.pass_time(DELAY)

move_servo(ACIK)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

while True:
  GPIO.output(TRIG, False)
  print "Olculuyor..."
  time.sleep(2)

  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)

  while GPIO.input(ECHO)==0:
    pulse_start = time.time()

  while GPIO.input(ECHO)==1:
    pulse_end = time.time()

  pulse_duration = pulse_end - pulse_start

  distance = pulse_duration * 17150
  distance = round(distance, 2)
  print distance
  if distance > 200 and distance < 400:
    print "Mesafe:",distance - 0.5,"cm"
    display.lcd_display_string(" -            - ",1)
  elif distance > 100 and distance < 200:
    display.lcd_display_string(" --         --  ",1)
  elif distance > 75 and distance < 100:
    display.lcd_display_string(" ---       ---  ",1)
  elif distance > 50 and distance < 75:
    display.lcd_display_string(" ----     ----  ",1)
  elif distance > 25 and distance < 50:
    display.lcd_display_string(" -----   -----  ",1)
  elif distance > 10 and distance < 25:                                                                                   
    display.lcd_display_string(" ------ ------  ",1)
  else:
    display.lcd_display_string("------DUR------",1)
    display.lcd_display_string(" Garaj Kapandi ",2)
    time.sleep(5)
    subprocess.call(["sudo","systemctl", "restart", "smart-lights"])
    move_servo(KAPA)
    time.sleep(5)
    break

quit()
