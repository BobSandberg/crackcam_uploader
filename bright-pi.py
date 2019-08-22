#!/usr/bin/python3
# This code will turn the bright pi lights on or off depending on command line params
# python3 bright-pi.py <state> --gain <gain> --pause <pause>
# state - (required) ON or OFF
# gain 	- (optional) 0 .. 15
# pause - (optional) 0 .. n seconds
#

from brightpi import *
import time
import sys
import argparse

parser = argparse.ArgumentParser("bright pi set lights")
parser.add_argument("state", help="ON or OFF.", choices=['ON', 'OFF'], default='OFF' )
parser.add_argument("--gain", help="gain value for light brightness.", type=int, choices=range(0,16), default=5, required=False )
parser.add_argument("--pause", help="pause in seconds.", type=int, choices=range(0,20), default = 2, required = False )
args = parser.parse_args()


brightPi = BrightPi()

brightPi.reset()

if args.state == "ON":
	print( "Turning lights on at gain={} and pause={} seconds".format(args.gain,args.pause) )

	leds = (1,2,3,4)
	brightPi.set_led_on_off(leds, ON)
	brightPi.set_gain(args.gain)
	time.sleep(args.pause)

else:
	print( "Turning lights off. Actually doing a reset()" )
	leds = [1, 2, 3, 4, 5, 6, 7, 8]
	brightPi.set_led_on_off(leds, OFF)

	brightPi.reset()
