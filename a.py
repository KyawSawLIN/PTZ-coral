#this is used in early stages of coding (only kept for memory) and refer to test.py if you needed complete code for angle control 

import serial
import time

ser = serial.Serial("COM4", 2400, timeout=5 )
while True:
 f = input()
 try:
    ser.write(bytes.fromhex('FF 07 00 02 3F 00 48'))
    time.sleep(2)
    ser.write(bytes.fromhex('FF 07 00 00 3F 3F 85'))
    time.sleep(0.1)
    ser.write(bytes.fromhex('FF 07 00 04 3F 00 4A'))
    time.sleep(2)
    #ser.write(bytes.fromhex('FF 07 00 4D 13 88 EF')) 
    #time.sleep(1)
    ser.write(bytes.fromhex('FF 07 00 4D 0B B8 17'))
    time.sleep(2)
    ser.write(bytes.fromhex('FF 07 00 4B 00 00 52'))
    ser.write(bytes.fromhex('FF 07 00 4B 46 4FE7'))
    ser.write(bytes.fromhex('FF 07 00 4B 8B38 15'))
    print(ser.read(7))
    
 except KeyboardInterrupt:
    break 

#ser.write(bytes.fromhex('FF 07 00 4B 88 88 62')) pan 1 cycle end 0 to 35999
#ser.write(bytes.fromhex('FF 07 00 4B 46 4F E7')) half in the middle 
#ser.write(bytes.fromhex('FF 07 00 4B 00 00 52')) zero position 


   #ser.write(bytes.fromhex('FF 07 00 4D 17 70 DB')) tilt 90 degree 0 to 6000
   #ser.write(bytes.fromhex('FF 07 00 4D 00 00 54')) tilt 0 degree 
   # ser.write(bytes.fromhex('FF 07 00 4D 0B B8 17')) half in the middle 