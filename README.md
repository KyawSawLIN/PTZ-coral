# PTZ-coral

see test.py for exact angle input control 

see sc.py for manual control continuous motion control 

tbd.py is to be deleted : nothing special and a.py is for rememberence 


# about hardware requirement 
PTZ in this project is PTS-303Z. (12V DC input) 
I use coral dev board UART pins to generate serial data. You can also use serial ports in PC(for PC, you may need usb-uart converter) or any microcontroller that include UART. 
As this PTZ platform works via RS485 serial hardware. You need UART(TTL) to RS485 converter(MAX485 chip) to control. 


# about software requirement 
pyserial is used to generate data. The generated data format should be in pelco-d format which is in 7 bytes hexadecimal. See pelco-d manual above. 

# about pelco-d format 
one of the bytes is checksum and you can calculate in the following website. 
https://www.scadacore.com/tools/programming-calculators/online-checksum-calculator/
