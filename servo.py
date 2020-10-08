#!usr/bin/python

import arduino_start
import time
DELAY = 1
MIN = 5
MAX = 150
MID = 40
servo = arduino_start.board.get_pin('d:9:s')
servo2 = arduino_start.board.get_pin('d:11:s')

def move_servo(v):
    servo.write(v)
    arduino_start.board.pass_time(DELAY)
def move_servo2(a):
    servo.write(a)
    arduino_start.board.pass_time(DELAY)
move_servo(MID)
time.sleep(5)
#move_servo2(175)
arduino_start.board.exit()
