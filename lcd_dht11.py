#!/usr/bin/python
# Import necessary libraries for communication and display use
#import sys
import Adafruit_DHT
import lcddriver
import time
import subprocess
import datetime
import sys

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = lcddriver.lcd()


# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
#if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
sensor = Adafruit_DHT.DHT11
pin = 14
#else:
 #   print('Usage: sudo ./Adafruit_DHT.py [11|22|2302] <GPIO pin number>')
 #   print('Example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO pin #4')
  #  sys.exit(1)

# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)                                                                                                                                                                                    # Un-comment the line below to convert the temperature to Fahrenheit.

# temperature = temperature * 9/5.0 + 32
# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!

if humidity is not None and temperature is not None:
    display.lcd_clear()
    time.sleep(1)
    display.lcd_display_string('Sicaklik: {0:0.01f} C  '.format(temperature,humidity), 1) # Write line of text to first line of display
    display.lcd_display_string("Nem:{1:0.01f}%         ".format(temperature,humidity), 2) # Write line of text to second line of display
else:
    display.lcd_display_string("Failed to get reading. Try again!", 1) 
    sys.exit(1)
time.sleep(2)
