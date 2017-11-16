#!/usr/bin/env python3

# code from ats1080
# Topic: Push Button Input - Falling Edge Detection
#
# file : button_test4.py

import logging
logging.basicConfig()

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from phue import Bridge

b = Bridge('172.24.1.112')
b.connect()
b.get_api()
lightnames = b.get_light_objects('name')

Brighter = 25 # GPIO-25, pin 16
Dimmer = 24 # GPIO-24, pin 12
Button = 16 # GPIO-16, pin 36
GPIO.setup(Button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Dimmer, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Brighter, GPIO.IN, pull_up_down=GPIO.PUD_UP)

LightState = lightnames["Pete"].on
Brightness = lightnames["Pete"].brightness


def onswitch_callback(Button):
	global LightState
	# only count Falling edges, discard anything else
	if GPIO.input(Button) == 0:
		if LightState == 1:
			lightnames["Pete"].on = False
		else:
			lightnames["Pete"].on = True
			Brightness = lightnames["Pete"].brightness

		LightState = lightnames["Pete"].on
		print ("Light is %d" % LightState)

	return # not needed, just for clarity

def brighter_callback(Brighter):
	global Brightness
	if GPIO.input(Brighter) == 0:
		if Brightness <= 234:
			Brightness += 20
		else:
			Brightness = 254

		print ("Bright to %d" % Brightness)
		lightnames["Pete"].brightness = Brightness
		
	return # not needed

def dimmer_callback(Dimmer):
	global Brightness
	if GPIO.input(Dimmer) == 0:
		if Brightness >= 20:
			Brightness -= 20
		else:
			Brightness = 20 

		print ("Dimming to %d" % Brightness)
		lightnames["Pete"].brightness = Brightness

	return # not needed

GPIO.add_event_detect(Button, GPIO.FALLING, callback=onswitch_callback)
GPIO.add_event_detect(Brighter, GPIO.FALLING, callback=brighter_callback)
GPIO.add_event_detect(Dimmer, GPIO.FALLING, callback=dimmer_callback)

try:
	print ("Light is %d" % LightState)
	print ("Brightness is %d" % Brightness)
	while True:
		pass

except KeyboardInterrupt:
	pass
finally:
	print ("\nRelease our used channel(s)")
	GPIO.cleanup([Button])

def main():
	print('Exiting')

if __name__ == '__main__':
    main()

