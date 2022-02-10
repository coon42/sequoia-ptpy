#!/usr/bin/env python
import ptpy
from ptpy import Canon
from time import sleep

camera = ptpy.PTPy()
info = camera.get_device_info()

print("Connected to the camera...")

with camera.session():
    print("Model: " + info.Model)
    print("Version: " + info.DeviceVersion)

    result = camera.eos_init_command('ffffffffff')
    if result.ResponseCode == 'OK':
        print("command enabled.")
    else:
        print("Error enabling command: %s" % result.ResponseCode)

