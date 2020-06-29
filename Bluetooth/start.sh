#!/bin/bash

bluetoothctl discoverable on
sudo rfcomm watch hci0 dp12cks34
