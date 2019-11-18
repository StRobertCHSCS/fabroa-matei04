from microbit import *
import time
import math
 
# Adapted from https://github.com/fizban99/microbit_ssd1306
OLED_ADDR = 0x3c
oled_screen = bytearray('b\x40') + bytearray(512)
 
def oled_initialize():
    for c in ([0xae], [0xa4], [0xd5, 0xf0], [0xa8, 0x3f], [0xd3, 0x00], [0 | 0x0], [0x8d, 0x14], [0x20, 0x00], [0x21, 0, 127], [0x22, 0, 63], [0xa0 | 0x1], [0xc8], [0xda, 0x12], [0x81, 0xcf], [0xd9, 0xf1], [0xdb, 0x40], [0xa6], [0xd6, 1], [0xaf]):
        i2c.write(OLED_ADDR, b'\x00' + bytearray(c))
 
def oled_set_pos(col=0, page=0):
    i2c.write(OLED_ADDR, b'\x00' + bytearray([0xb0 | page]))
    c1, c2 = col * 2 & 0x0F, col >> 3
    i2c.write(OLED_ADDR, b'\x00' + bytearray([0x00 | c1]))
    i2c.write(OLED_ADDR, b'\x00' + bytearray([0x10 | c2]))
 
def oled_clear_screen(c=0):
    global oled_screen
    oled_set_pos()
    for i in range(1, 513):
        oled_screen[i] = 0
    oled_draw_screen()
 
def oled_draw_screen():
    global oled_screen
    oled_set_pos()
    i2c.write(OLED_ADDR, oled_screen)
 
def oled_add_text(x, y, text):
    global oled_screen
    for i in range(0, min(len(text), 12 - x)):
        for c in range(0, 5):
            col = 0
            for r in range(1, 6):
                p = Image(text[i]).get_pixel(c, r - 1)
                col = col | (1 << r) if (p != 0) else col
            ind = x * 10 + y * 128 + i * 10 + c * 2 + 1
            oled_screen[ind], oled_screen[ind + 1] = col, col
    oled_set_pos(x * 5, y)
    ind0 = x * 10 + y * 128 + 1
    i2c.write(OLED_ADDR, b'\x40' + oled_screen[ind0 : (ind+1)])
 
#allow overflow to go onto the next line
def oled_add_text_new_line(x, y, text):
    length_text = len(text)
    separated_text = []
    counter = 0
    num_of_lines = math.ceil(length_text/12)
    letters_in_line = 12
     
    for line in range(0,num_of_lines):
        separated_text.append([])
        #separated_text[line].append(y*(line+1))
        for l in range(0,letters_in_line):
            separated_text[line].append(text[letters_in_line*line+l])
            counter +=1
            if counter == length_text:
                break
     
    #draw letters
    for i in range(0,len(separated_text)):
        oled_add_text(x,y+i,separated_text[i])
         
 
# Screen divided into 12 columns and 4 rows
 
oled_initialize()
oled_clear_screen()
 
# Start Simple Alarm Box Code here 
 
#pins
CrashSensor_pin = pin0
LED_pin = pin8
 
#set up crash sensor
CrashSensor_pin.set_pull(CrashSensor_pin.PULL_UP)
 
#other variables
has_text = False
 
while True:
    if CrashSensor_pin.read_digital() == 1:
        if has_text == False : #checks if oled screen has the message already, if not add it
            oled_add_text_new_line(0, 0, "wavy!")from microbit import *
import time
import math
 
# Adapted from https://github.com/fizban99/microbit_ssd1306
OLED_ADDR = 0x3c
oled_screen = bytearray('b\x40') + bytearray(512)
 
def oled_initialize():
    for c in ([0xae], [0xa4], [0xd5, 0xf0], [0xa8, 0x3f], [0xd3, 0x00], [0 | 0x0], [0x8d, 0x14], [0x20, 0x00], [0x21, 0, 127], [0x22, 0, 63], [0xa0 | 0x1], [0xc8], [0xda, 0x12], [0x81, 0xcf], [0xd9, 0xf1], [0xdb, 0x40], [0xa6], [0xd6, 1], [0xaf]):
        i2c.write(OLED_ADDR, b'\x00' + bytearray(c))
 
def oled_set_pos(col=0, page=0):
    i2c.write(OLED_ADDR, b'\x00' + bytearray([0xb0 | page]))
    c1, c2 = col * 2 & 0x0F, col >> 3
    i2c.write(OLED_ADDR, b'\x00' + bytearray([0x00 | c1]))
    i2c.write(OLED_ADDR, b'\x00' + bytearray([0x10 | c2]))
 
def oled_clear_screen(c=0):
    global oled_screen
    oled_set_pos()
    for i in range(1, 513):
        oled_screen[i] = 0
    oled_draw_screen()
 
def oled_draw_screen():
    global oled_screen
    oled_set_pos()
    i2c.write(OLED_ADDR, oled_screen)
 
def oled_add_text(x, y, text):
    global oled_screen
    for i in range(0, min(len(text), 12 - x)):
        for c in range(0, 5):
            col = 0
            for r in range(1, 6):
                p = Image(text[i]).get_pixel(c, r - 1)
                col = col | (1 << r) if (p != 0) else col
            ind = x * 10 + y * 128 + i * 10 + c * 2 + 1
            oled_screen[ind], oled_screen[ind + 1] = col, col
    oled_set_pos(x * 5, y)
    ind0 = x * 10 + y * 128 + 1
    i2c.write(OLED_ADDR, b'\x40' + oled_screen[ind0 : (ind+1)])
 
#allow overflow to go onto the next line
def oled_add_text_new_line(x, y, text):
    length_text = len(text)
    separated_text = []
    counter = 0
    num_of_lines = math.ceil(length_text/12)
    letters_in_line = 12
     
    for line in range(0,num_of_lines):
        separated_text.append([])
        #separated_text[line].append(y*(line+1))
        for l in range(0,letters_in_line):
            separated_text[line].append(text[letters_in_line*line+l])
            counter +=1
            if counter == length_text:
                break
     
    #draw letters
    for i in range(0,len(separated_text)):
        oled_add_text(x,y+i,separated_text[i])
         
 
# Screen divided into 12 columns and 4 rows
 
oled_initialize()
oled_clear_screen()
 
# Start Simple Alarm Box Code here 
 
#pins
CrashSensor_pin = pin0
LED_pin = pin8
 
#set up crash sensor
CrashSensor_pin.set_pull(CrashSensor_pin.PULL_UP)
 
#other variables
has_text = False
 
while True:
    if CrashSensor_pin.read_digital() == 1:from microbit import *
import time
import math
 
# Adapted from https://github.com/fizban99/microbit_ssd1306
OLED_ADDR = 0x3c
oled_screen = bytearray('b\x40') + bytearray(512)
 
def oled_initialize():
    for c in ([0xae], [0xa4], [0xd5, 0xf0], [0xa8, 0x3f], [0xd3, 0x00], [0 | 0x0], [0x8d, 0x14], [0x20, 0x00], [0x21, 0, 127], [0x22, 0, 63], [0xa0 | 0x1], [0xc8], [0xda, 0x12], [0x81, 0xcf], [0xd9, 0xf1], [0xdb, 0x40], [0xa6], [0xd6, 1], [0xaf]):
        i2c.write(OLED_ADDR, b'\x00' + bytearray(c))
 
def oled_set_pos(col=0, page=0):
    i2c.write(OLED_ADDR, b'\x00' + bytearray([0xb0 | page]))
    c1, c2 = col * 2 & 0x0F, col >> 3
    i2c.write(OLED_ADDR, b'\x00' + bytearray([0x00 | c1]))
    i2c.write(OLED_ADDR, b'\x00' + bytearray([0x10 | c2]))
 
def oled_clear_screen(c=0):
    global oled_screen
    oled_set_pos()
    for i in range(1, 513):
        oled_screen[i] = 0
    oled_draw_screen()
 
def oled_draw_screen():
    global oled_screen
    oled_set_pos()
    i2c.write(OLED_ADDR, oled_screen)
 
def oled_add_text(x, y, text):
    global oled_screen
    for i in range(0, min(len(text), 12 - x)):
        for c in range(0, 5):
            col = 0
            for r in range(1, 6):
                p = Image(text[i]).get_pixel(c, r - 1)
                col = col | (1 << r) if (p != 0) else col
            ind = x * 10 + y * 128 + i * 10 + c * 2 + 1
            oled_screen[ind], oled_screen[ind + 1] = col, col
    oled_set_pos(x * 5, y)
    ind0 = x * 10 + y * 128 + 1
    i2c.write(OLED_ADDR, b'\x40' + oled_screen[ind0 : (ind+1)])
 
#allow overflow to go onto the next line
def oled_add_text_new_line(x, y, text):
    length_text = len(text)
    separated_text = []
    counter = 0
    num_of_lines = math.ceil(length_text/12)
    letters_in_line = 12
     
    for line in range(0,num_of_lines):
        separated_text.append([])
        #separated_text[line].append(y*(line+1))
        for l in range(0,letters_in_line):
            separated_text[line].append(text[letters_in_line*line+l])
            counter +=1
            if counter == length_text:
                break
     
    #draw letters
    for i in range(0,len(separated_text)):
        oled_add_text(x,y+i,separated_text[i])
         
 
# Screen divided into 12 columns and 4 rows
 
oled_initialize()
oled_clear_screen()
 
# Start Simple Alarm Box Code here 
 
#pins
CrashSensor_pin = pin0
LED_pin = pin8
 
#set up crash sensor
CrashSensor_pin.set_pull(CrashSensor_pin.PULL_UP)
 
#other variables
has_text = False
 
while True:
    if CrashSensor_pin.read_digital() == 1:
        if has_text == False : #checks if oled screen has the message already, if not add it
            oled_add_text_new_line(0, 0, "Your treasure is safe")
            has_text = True
        LED_pin.write_digital(1)
         
    else:
        #clear oled screen 
        oled_clear_screen()
        has_text = False
         
        #make LED blink
        LED_pin.write_digital(0)
        time.sleep(0.1)
        LED_pin.write_digital(1)
        time.sleep(0.1)    
        if has_text == False : #checks if oled screen has the message already, if not add it
            oled_add_text_new_line(0, 0, "Your treasure is safe")
            has_text = True
        LED_pin.write_digital(1)
         
    else:
        #clear oled screen 
        oled_clear_screen()
        has_text = False
         
        #make LED blink
        LED_pin.write_digital(0)
        time.sleep(0.1)
        LED_pin.write_digital(1)
        time.sleep(0.1)    
            has_text = True
        LED_pin.write_digital(1)
         
    else:
        #clear oled screen 
        oled_clear_screen()
        has_text = False
         
        #make LED blink
        LED_pin.write_digital(0)
        time.sleep(0.1)
        LED_pin.write_digital(1)
        time.sleep(0.1)    