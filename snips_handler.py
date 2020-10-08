#encoding: utf-8
from __future__ import unicode_literals

import datetime
import json
import subprocess
import RPi.GPIO as GPIO
import os
import sys
import arduino_start
import lcddriver
import paho.mqtt.client as mqtt
import time


DELAY = 1
AC=135
KAPA=45

board = arduino_start.board
display = lcddriver.lcd()
display.lcd_clear()
pinbuzz = board.get_pin("d:8:o")
pinalev = board.get_pin("d:10:i")
servo = board.get_pin("d:9:s")

def move_servo(v):
    servo.write(v)
    arduino_start.board.pass_time(DELAY)

move_servo(KAPA)
fromtimestamp = datetime.datetime.fromtimestamp

# MQTT client to connect to the bus
mqtt_client = mqtt.Client()
HOST = "localhost"
PORT = 1883
HOTWORD_DETECTED = "hermes/hotword/default/detected"
HOTWORDS_ON = {"open","open2"}
HOTWORDS_OFF = {"close", "close2"}
HOTWORDS_ISI = {"sicaklik"}
HOTWORDS_GRJO = {"garajo"}
HOTWORDS_GRJC = {"garajc"}
HOTWORDS_FANO = {"fanacik"}
HOTWORDS_FANC = {"fankapali"}
HOTWORDS_KAPO = {"kapiac"}
HOTWORDS_KAPC = {"kapika"}
# Subscribe to the important messages
def on_connect(client, userdata, flags, rc):
    mqtt_client.subscribe(HOTWORD_DETECTED)

# Process a message as it arrives
def on_message(client, userdata, msg):
    if not msg.topic == HOTWORD_DETECTED:
	return

    payload = json.loads(msg.payload)
    model_id = payload["modelId"]
    if model_id in HOTWORDS_ON:
	display.lcd_clear()
	board.digital[4].write(1)
	subprocess.call(["/home/pi/isik_commands/isik.py", "on"])
	time.sleep(2)
    elif model_id in HOTWORDS_OFF:
	display.lcd_clear()
	board.digital[4].write(0)
	subprocess.call(["/home/pi/isik_commands/isik.py", "off"])
	time.sleep(2)
    elif model_id in HOTWORDS_ISI:
	display.lcd_clear()
	subprocess.call(["/home/pi/isik_commands/lcd_dht11.py"])
	time.sleep(10)
    elif model_id in HOTWORDS_GRJO:
	move_servo(AC)
	subprocess.call(["/home/pi/isik_commands/mesafe.py"])
    elif model_id in HOTWORDS_GRJC:
	move_servo(KAPA)
	display.lcd_clear()
	display.lcd_display_string("  Garaj Kapali  ",1)
	time.sleep(2)
    elif model_id in HOTWORDS_FANO:
        subprocess.call(["/home/pi/isik_commands/fan.py", "off"])
        time.sleep(2)
    elif model_id in HOTWORDS_FANC:
        subprocess.call(["/home/pi/isik_commands/fan.py", "on"])
        time.sleep(2)
    elif model_id in HOTWORDS_KAPO:
        subprocess.call(["/home/pi/isik_commands/servopi.py", "on"])
        time.sleep(2)
    elif model_id in HOTWORDS_KAPC:
        subprocess.call(["/home/pi/isik_commands/servopi.py", "off"])
        time.sleep(2)
    else:
        print("Unmapped hotword model_id: %s" % model_id)


if __name__ == '__main__':
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(HOST, PORT)
    mqtt_client.loop_start()
    x=0
    loop_flag=1
    while loop_flag != 0:
        if pinalev.read() != 1:
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
	 display.lcd_clear()
         display.lcd_display_string("Sistem calisiyor", 1)
         display.lcd_display_string(" Durum bekliyor ", 2)
         time.sleep(3)
         display.lcd_clear()
         time.sleep(3)
         continue
