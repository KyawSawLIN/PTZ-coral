import serial
import time

ser = serial.Serial("COM4", 2400, timeout=10)  # 2400 baud rate

f = open("code.py","a")

for i in range(120): #120 means 120 lines of code 
 str = ser.readline()
 str = str.decode('utf-8')
 f.write( str )
