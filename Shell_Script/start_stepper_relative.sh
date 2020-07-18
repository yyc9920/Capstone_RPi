#!/bin/bash

bluetoothctl discoverable on
sudo rfcomm watch hci0 dp12cks34 &
# Waiting for bluetooth device to be connected in background
# dp12cks34 => chage this to your RPi password
python3 /home/pi/Capstone_RPi/Tracker_hor/multiple_tracker_stepper_hor_relative.py
# Track face with stepper motor
