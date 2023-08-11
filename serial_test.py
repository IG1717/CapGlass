# Importing Libraries
import serial
import time
import main

arduino = serial.Serial(port='/dev/cu.usbmodem14301', baudrate=115200, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
while True:
    value = write_read(main.main())
    print(value) # printing the value