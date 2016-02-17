############################################################
# P1 Info Radiator
# https://github.com/TinkurLab/P1InfoRadiator
#
# Created by Tinkurlab www.tinkurlab.com
############################################################

import requests
import time
import os
import RPi.GPIO as io 
io.setmode(io.BCM)

power_pin = 23
io.setup(power_pin, io.OUT)
io.output(power_pin, False)

def checkStatus():
	#Get request from API URL
	r = requests.get('https://tinkurradiator.herokuapp.com/get')

	#Evaluate response and determine status
	if r.text == "0":
		status = "all is well"
		print "status is " + status
	elif r.text == "1":
		status = "P1"
		print "status is " + status
		io.output(power_pin, True)
		os.system('omxplayer "tng_red_alert2.mp3"')
		time.sleep(30)
		io.output(power_pin, False)
	else:
		status = "no sure..."
		print "status is " + status

	#Return status
	return status

###############
#Main
###############

#Forever loop w/ sleep to check status
i = 0
while i < 1:
   checkStatus()
   time.sleep(10)
