#!/usr/bin/env python3

import signal
import threading
import queue
import sys
import os
from phue import Bridge
import RPi.GPIO as GPIO


q = queue.Queue()
bridge = Bridge('172.24.1.26')
bridge.connect()
bridge.get_api()
g_bulbs = bridge.get_light_objects('name')
g_bulb1 = g_bulbs[sys.argv[1]]
g_bulb2 = g_bulbs[sys.argv[2]]
g_brightness = 255


def doEvent(pad):
	global g_bulb1,g_state1,g_brightness,g_bulb1,g_state1
	try:
		g_state1 = g_bulb1.on
		g_state2 = g_bulb2.on
		print ("%s state is %d" % (g_bulb1, g_state1))
		print ("%s state is %d" % (g_bulb2, g_state2))
	except:
		print ("Exception checking state, state not changed...")

	if pad == "Enter":
		if g_state1 == True:
			print ("Turning %s off" % g_bulb1)
			try:
				g_bulb1.on = False
			except:
				print ("Exception turning primary light off")
			g_state1 = False

		elif g_state1 == False:
			print ("Turning %s on" % g_bulb1)
			try:
				g_bulb1.on = True
				g_bulb1.brightness = g_brightness
			except:
				print ("Exception attempting to turn on %s" % g_bulb1)
			g_state1 = True

	elif pad == "Back":
		if g_state2 == True:
			print ("Turning %s off" % g_bulb2)
			try:
				g_bulb2.on = False
			except:
				print ("Exception turning secondary light off")
			g_state2 = False
		elif g_state2 == False:
			print ("Turning %s on" % g_bulb2)
			try:
				g_bulb2.on = True
				g_bulb2.brightness = g_brightness
			except:
				print ("Exception attempting to turn on %s" % g_bulb2)
			g_state2 = True
	else:
		if pad == "A":
			g_brightness = 20
		elif pad == "B":
			g_brightness = 100
		elif pad == "C":
			g_brightness = 175
		elif pad == "D":
			g_brightness = 254
		if g_state1 == True:
			try:
				g_bulb1.brightness = g_brightness
			except:
				print ("Exception setting brightness based on pad input")
		if g_state2 == True:
			try:
				g_bulb2.brightness = g_brightness
			except:
				print ("Exception setting brightness based on pad input")

def setstate(index, state):
	global g_state1, g_state2
	if state == True:
		if index == 1:
			g_state1 = state
		else:
			g_state2 = state
	else:
		if index == 1:
			g_state1 = state
		else:
			g_state2 = state

def checkit():
	global g_brightness1,g_bulb1,g_state1,g_brightness2,g_bulb2,g_state2
    bright = 0
    
	try: 
		state1 = g_bulb1.on
		state2 = g_bulb2.on
		bright = g_bulb1.brightness
	except:
		state1 = g_state1
		state2 = g_state2
		bright = g_brightness

	if state1 != g_state1:
		print ("State change from %d to %d" % (g_state1, state1))
		setstate(1, state1)

	if state2 != g_state2:
		print ("State change from %d to %d" % (g_state2, state2))
		setstate(2, state2)

	setbrightness(g_brightness)

	while not q.empty():
		print ("Handling queue")
		t = q.get()
		doEvent(t)

	t = threading.Timer(1.0, checkit)
	t.start()

def main():
	global g_bulb1, g_bulb2, g_state1, g_state2, g_brightness
	g_state1 = False;
	g_state2 = False;
	g_brightness = 0;
	try:
		g_state1 = g_bulb1.on
		g_state2 = g_bulb2.on
		g_brightness = g_bulb1.brightness
		print ("%s state is %d" % (g_bulb1, g_state1))
		print ("%s state is %d" % (g_bulb2, g_state2))
		print ("%s brightness is %d" % (g_bulb1, g_brightness))
	except:
		print ("Startup Connection error")

	setstate(1, g_state1)
	setstate(2, g_state2)
	setbrightness(g_brightness)
	checkit()
	signal.pause()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		touchphat.all_off()
		print('Interrupted')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)