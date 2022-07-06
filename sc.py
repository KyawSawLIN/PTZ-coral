#software control of PTZ 
import serial
import time

ser = serial.Serial("COM4", 2400)

def toHex(dec):  # convert dec to hex without '0x' included
    digits = "0123456789ABCDEF"
    x = (dec % 16)
    rest = dec // 16
    if (rest == 0):
        return digits[x]
    return toHex(rest) + digits[x]


def print_position(a):

    q1 = toHex(a[4])
    q2 = toHex(a[5])

    q_3 = '{0:0>2s}{1:0>2s}'.format(q1, q2)
    q_final = int(q_3, 16) // 100
    return q_final


def read_position():

    ser.write(bytes.fromhex('FF 07 00 51 00 00 58'))
    #time.sleep(1)
    pan_read = ser.read(7)

    ser.write(bytes.fromhex('FF 07 00 53 00 00 5A'))
    #time.sleep(1)
    tilt_read = ser.read(7)
    
    return pan_read, tilt_read

while True: 
 d = input('decision: left(l) | right(r) | up(u) | down(d) | up right(ur) | up left (ul) | down right(dr) | down left(dl) | STOP(s) | query position(p): ')
 try:

    if d=='r':
     #while True:
      print('pan right')
      ser.write(bytes.fromhex('FF 07 00 02 3F 00 48'))
    if d=='l':
        #while True:
         print('pan left')
         ser.write(bytes.fromhex('FF 07 00 04 3F 00 4A'))
         #ser.write(b'\0xFF\0x07\0x00\0x04\0x3F\0x00\0x4A')
    if d=='u':
        #while True:
         print('pan left')
         ser.write(bytes.fromhex('FF 07 00 08 00 3F 4E'))
         #ser.write(b'\0xFF\0x07\0x00\0x08\0x00\0x3F\0x4E')
    if d=='d':
        #while True:
         print('tilt down')
         ser.write(bytes.fromhex('FF 07 00 16 00 3F 5C'))
    if d=='dl':
        #while True:
            print("tilt down pan left")
            ser.write(bytes.fromhex('FF 07 00 14 32 32 99'))
    if d=='dr':
        #while True:
            print("tilt down pan right")
            ser.write(bytes.fromhex('FF 07 00 12 3F 3F 97'))
    if d=='ul':
        #while True:
            print("tilt up pan left")
            ser.write(bytes.fromhex('FF 07 00 0C 3F 3F 91'))
    if d=='ur':
        #while True:
            print("tilt up pan right")
            ser.write(bytes.fromhex('FF 07 00 0A 3F 3F 8F'))
    if d=='s':
        #while True:
            print("STOP")
            ser.write(bytes.fromhex('FF 07 00 00 3F 3F 85'))
    if d=='z':
        print('zero positon')
        ser.write(bytes.fromhex('FF 07 00 49 00 00 50'))
    if d == 'p':
        reading = read_position()
        print('current position ...\t pan: {0} ||  tilt: {1}'.format(
        print_position(reading[0]), print_position(reading[1])))

 except KeyboardInterrupt:
    continue  
