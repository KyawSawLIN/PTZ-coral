#software control of PTZ 
import serial

ser = serial.Serial("/dev/ttyUSB0", 2400)

while True: 
 d = input('decision: left(l) \n  right(r) \n up(u) \n down(d): ')
 try:
    if d=='r':
     while True:
      print('pan right')
      ser.write(bytearray.fromhex('FF 01 00 02 20 00 23'))
    if d=='l':
        while True:
         print('pan left')
         ser.write(bytearray.fromhex('FF 01 00 04 3F 00 44'))
    if d=='u':
        while True:
         print('pan left')
         ser.write(bytearray.fromhex('FF 01 00 08 00 3F 48'))
    if d=='d':
        while True:
         print('pan left')
         ser.write(bytearray.fromhex('FF 01 00 10 20 00 31'))
    if d=='d':
        while True:
         print('pan left')
         ser.write(bytearray.fromhex('FF 01 00 10 20 00 31'))
 except KeyboardInterrupt:
    continue 
 
