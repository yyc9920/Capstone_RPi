# test code to fix Issue#1
import serial
import threading
import time
from pathlib import Path

b_device = Path("/dev/rfcomm0")

exception_flag = 0

def getCoord():
	while True:
            if(b_device.exists() == True):
                    # Read Coordinates String via Bluetooth Communication
                    try:
                            ser = serial.Serial('/dev/rfcomm0')
                            coord = ser.readline()
                            test = ser.readline()
                            coord = coord.decode('utf-8')
                            coord = coord[0:-2]
                    except serial.serialutil.SerialException as e:
                            print(e)
                            print("Bluetooth connection lost")
                            exception_flag = 1
                            break
                    else:
                            pass
            else:
                    continue

            print("coord :")
            print(coord)
            print("test")
            print(test)

while True:
    if(b_device.exists() == True):
        getCoord()
    else:
        print("Bluetooth not connected")
        time.sleep(5)
