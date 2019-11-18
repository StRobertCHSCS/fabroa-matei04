#Name:		microbit_logic_assignment3.py
#Purpose:	to make a compass using a microbit


#Author:	gornic.M and harold.P

#Created:	30/10/2019

from microbit import *

# Starts calibrating by tilting microbit
compass.calibrate()

# Try to keep the needle pointed in the right diretion
while True:
    sleep(80)
    needle = ((15 - compass.heading()) // 30) % 12
    display.show(Image.ALL_CLOCKS[needle])