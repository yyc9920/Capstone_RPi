#!/bin/bash

bluetoothctl discoverable on
sudo rfcomm watch hci0 dp12cks34
# Waiting for bluetooth device to be connected
# dp12cks34 => chage this to your RPi password

python3 /home/pi/Capstone_design/Tracker_hor/multiple_tracker_hor.py
