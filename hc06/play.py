import keyboard
import time
from pyfirmata import Arduino

# enR = 5
# enL = 6
# M1L = 8
# M2L = 7
# M1R = 2
# M2R = 4

speed  = 0.6

board = Arduino('COM23')

enR = board.get_pin('d:5:p')
enL = board.get_pin('d:6:p')
M1L = board.get_pin('d:8:o')
M2L = board.get_pin('d:7:o')
M1R = board.get_pin('d:2:o')
M2R = board.get_pin('d:4:o')




def forward():

    enR.write(speed)
    M1R.write(0)
    M2R.write(1)
    enL.write(speed)
    M1L.write(1)
    M2L.write(0)

def backward():
    enR.write(speed)
    M1R.write(1)
    M2R.write(0)
    enL.write(speed)
    M1L.write(0)
    M2L.write(1)

def right():
    enR.write(speed)
    M1R.write(1)
    M2R.write(0)
    enL.write(speed)
    M1L.write(1)
    M2L.write(0)

def left():
    enR.write(speed)
    M1R.write(0)
    M2R.write(1)
    enL.write(speed)
    M1L.write(0)
    M2L.write(1)

def stop():
    enR.write(0)
    M1R.write(0)
    M2R.write(1)
    enL.write(0)
    M1L.write(0)
    M2L.write(1)


print("""
====================================================
=================== W ==============================
======== A ======== S ======== D====================
====================================================
          """)

while True:
    key = keyboard.read_key()

    if key == 'w':
        forward()
        print('forward')
        time.sleep(0.1)

    if key == 'a':
        left()
        print('left')
        time.sleep(0.1)
    if key == 's':
        backward()
        print('backward')
        time.sleep(0.1)
    if key == 'd':
        right()
        print('right')
        time.sleep(0.1)
    if key == 'q':
        stop()
        print('stop')
        time.sleep(0.1)