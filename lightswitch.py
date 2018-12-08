#!/usr/bin/env python3

import signal
import time
import threading
import queue
import sys
import touchphat
from phue import Bridge

touchphat.auto_led = False	
q = queue.Queue()
bridge = Bridge('172.24.1.26')
bridge.connect()
bridge.get_api()
g_bulbs = bridge.get_light_objects('name')
g_state = g_bulbs[sys.argv[1]].on
g_brightness = g_bulbs[sys.argv[1]].brightness
print ("LightState is %d" % g_state)
print ("Lightbright is %d" % g_brightness)

def setbrightness(bright):
	if bright < 50:
		touchphat.led_on("A")
	elif bright < 125:
		touchphat.led_on("B")
	elif bright < 200:
		touchphat.led_on("C")
	else:
		touchphat.led_on("D")

def doEvent(pad):
	global g_bulbs,g_state,g_brightness
	g_state = g_bulbs[sys.argv[1]].on
	print ("Light state is %d" % g_state)
	if pad == "Enter":
		g_state = True 
		g_bulbs[sys.argv[1]].on = g_state
		g_bulbs[sys.argv[1]].brightness = g_brightness
		setbrightness(g_brightness)
	elif pad == "Back":
		touchphat.led_on("Enter")
		g_state = False
		g_bulbs[sys.argv[1]].on = g_state
	else:
		touchphat.led_off("A")
		touchphat.led_off("B")
		touchphat.led_off("C")
		touchphat.led_off("D")
		if pad == "A":
			g_brightness = 20
		elif pad == "B":
			g_brightness = 100
		elif pad == "C":
			g_brightness = 175
		elif pad == "D":
			g_brightness = 254
		touchphat.led_on(pad)
		if g_state == False:
			g_bulbs[sys.argv[1]].on = True 
		g_bulbs[sys.argv[1]].brightness = g_brightness

@touchphat.on_touch(['Back','A','B','C','D','Enter'])
def handle_touch(event):
	q.put(event.name)

def setstate(state):
	global g_state

	if state == True:
		touchphat.led_on("Back")
	else:
		touchphat.all_off()
		touchphat.led_on("Enter")
	g_state = state

def checkit():
	global g_brightness,g_bulbs,g_state

	try: 
		state = g_bulbs[sys.argv[1]].on
		bright = g_bulbs[sys.argv[1]].brightness
	except:
		state = g_state
		bright = g_brightness

	if state != g_state:
		print ("State change from %d to %d" % (g_state, state))
		setstate(state)

	if bright != g_brightness:
		print ("Brightness change from %d to %d" % (g_brightness, bright))
		g_brightness = bright
		setbrightness(bright)

	while not q.empty():
		t = q.get()
		doEvent(t)

	t = threading.Timer(1.0, checkit)
	t.start()

try:
	setstate(g_state)
	if g_state == True:
		setbrightness(g_brightness)

	checkit()
	signal.pause()
except KeyboardInterrupt:
	touchphat.all_off()
	sys.exit(0)
except:
	print("Unknown Error")
	sys.exit(0)
