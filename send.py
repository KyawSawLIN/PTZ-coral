
import serial
import time

ser = serial.Serial("COM5", 2400)  # 2400 baud rate
f = open("test.py","r")
 
str = f.readlines()

for lines in str:
    ser.write(bytearray(lines,'utf-8'))

f.close()