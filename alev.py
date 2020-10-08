#!usr/bin/python
import arduino_start
import time
import lcddriver
import sys


board = arduino_start.board
display = lcddriver.lcd()

pin = board.get_pin('d:10:i')
pinbuzz = board.get_pin('d:8:o')
x=0

while True:
	if pin.read() != 1:
	 if x == 0: continue
	 else: x=1	
	 print("alev")
	 pinbuzz.write(1)
	 display.lcd_display_string("-----DIKKAT-----", 1)
	 display.lcd_display_string("      ALEV      ", 2)
	 time.sleep(1)
	 display.lcd_clear()
	 pinbuzz.write(0)
	 time.sleep(1)
	else:
	 x=1
	 display.lcd_display_string("Sistem calisiyor", 1)
	 display.lcd_display_string("  Durum normal  ", 2)
	 time.sleep(1)
	 display.lcd_clear()
	 time.sleep(1)
	 continue
