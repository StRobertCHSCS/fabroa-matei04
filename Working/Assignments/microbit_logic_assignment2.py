#Name:		microbit_logic_assignment2.py
#Purpose:	we created a program that displays the emotions of the microbit when tickled in a certain spot


#Author:	gornic.M and harold.P

#Created:	30/10/2019


from microbit import *

while True:
     if pin0.is_touched():
        display.show(Image.SAD)
     else:
        if pin0.is_touched and pin1.is_touched():
            display.show(Image.HAPPY)