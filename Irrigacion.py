# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import Raspberry Pi's GPIO control library
import RPi.GPIO as GPIO
# Imports sleep functon
from time import sleep

# Set up Rpi.GPIO library to use physical pin numbers
GPIO.setmode(GPIO.BCM)
# Set up pin no. 32 as output and default it to low
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)

# Blink the led
while True: # Forever
	sleep(0.5)                 # Wait 500ms
	GPIO.output(25, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(25, GPIO.LOW)  # Turn led off