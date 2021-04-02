import serial
import os
import pigpio

pi = pigpio.pi()
ser = serial.Serial("/dev/serial0", 115200)
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE

while True:
    frame = bytearray()
    received_data = None
    received_data = ser.read()  # read serial port
    intReceived = int.from_bytes(received_data, byteorder='little')
    if intReceived == 32:
        frame.extend(received_data)  # add the header
        # read the next 31 bytes of the frame (to make a 32 byte frame size)
        nextBytes = ser.read(31)
        # add the readed 31 bytes to the frame bytearray
        frame.extend(nextBytes)

        ch1byte = bytearray()
        ch1byte.append(frame[2])
        ch1byte.append(frame[3])
        ch1 = int.from_bytes(ch1byte, byteorder='little')

        ch2byte = bytearray()
        ch2byte.append(frame[4])
        ch2byte.append(frame[5])
        ch2 = int.from_bytes(ch2byte, byteorder='little')

        ch3byte = bytearray()
        ch3byte.append(frame[6])
        ch3byte.append(frame[7])
        ch3 = int.from_bytes(ch3byte, byteorder='little')

        ch4byte = bytearray()
        ch4byte.append(frame[8])
        ch4byte.append(frame[9])
        ch4 = int.from_bytes(ch4byte, byteorder='little')

        ch5byte = bytearray()
        ch5byte.append(frame[10])
        ch5byte.append(frame[11])
        ch5 = int.from_bytes(ch5byte, byteorder='little')

        ch6byte = bytearray()
        ch6byte.append(frame[12])
        ch6byte.append(frame[13])
        ch6 = int.from_bytes(ch6byte, byteorder='little')

        # flysky I6-i6 has only 6 channels - ends here

        ch7byte = bytearray()
        ch7byte.append(frame[14])
        ch7byte.append(frame[15])
        ch7 = int.from_bytes(ch7byte, byteorder='little')

        ch8byte = bytearray()
        ch8byte.append(frame[16])
        ch8byte.append(frame[17])
        ch8 = int.from_bytes(ch8byte, byteorder='little')

        ch9byte = bytearray()
        ch9byte.append(frame[18])
        ch9byte.append(frame[19])
        ch9 = int.from_bytes(ch9byte, byteorder='little')

        ch10byte = bytearray()
        ch10byte.append(frame[20])
        ch10byte.append(frame[21])
        ch10 = int.from_bytes(ch10byte, byteorder='little')

        ch11byte = bytearray()
        ch11byte.append(frame[22])
        ch11byte.append(frame[23])
        ch11 = int.from_bytes(ch11byte, byteorder='little')

        ch12byte = bytearray()
        ch12byte.append(frame[24])
        ch12byte.append(frame[25])
        ch12 = int.from_bytes(ch12byte, byteorder='little')

        ch13byte = bytearray()
        ch13byte.append(frame[26])
        ch13byte.append(frame[27])
        ch13 = int.from_bytes(ch13byte, byteorder='little')

        print("ch1=", ch1,  "ch2=", ch2, "ch3=", ch3, "ch4=", ch4, "ch5=", ch5, "ch6=", ch6, "ch7=", ch7, "ch6=", ch6, "ch7=", ch7, "ch8=", ch8,
              "ch9=", ch9, "ch10=", ch10, "ch11=", ch11, "ch12=", ch12, "ch13=", ch13)

        # now - do whatever you need with the channels, like controlling a servo with PWM
        # channels go from 1000 to 2000 so you may have to "normalize" the values for some servos (500-1500)
        servo = ch1-500
        # dont pass the max or min or PWM libraries may brake
        if servo < 500:
            servo = 500
        if servo > 1500:
            servo = 1500
        pi.set_servo_pulsewidth(14, servo)
