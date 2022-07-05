import sys

locate_python = sys.exec_prefix

print(locate_python)

def toHex(dec):
    digits = "0123456789ABCDEF"
    x = (dec % 16)
    rest = dec // 16
    if (rest == 0):
        return digits[x]
    return toHex(rest) + digits[x]

def checksum(str):
 c=0
 for i in range(5):
     c = c + str[i]
 c = c % 256
 print('checksum value = ', toHex(c))
 return toHex(c)

a = '07004B0000'
b = bytes.fromhex('07 00 4B 00 00')
d = bytes.fromhex('07 00 4B 88 88')

print(checksum(d))




# Two hex digits is one byte. You're looking for a checksum which produces one byte.

# Obviously, you've got a simple additive checksum (sum the bytes of the input), and an xor of the input bytes.
