'''
-------------------------------------------------------------------------------
#Name:		cpt2_code.py
#Purpose:    indicates when given time on consumer is fullfilled

#Author:	Gornic.M and Harold.P

#Created:	date in 23/01/2020
------------------------------------------------------------------------------
'''






from microbit import *
 
#pins
PIR_pin = pin0
LED_pin = pin1
 
while True:
    # if PIR Sensor detects motion fromt the hour glass, the light turns on

    if PIR_pin.read_digital(): 
        LED_pin.write_digital(1)
    else:
        LED_pin.write_digital(0)
        #If the subject did not spend all the given screen time, the light does not turn on