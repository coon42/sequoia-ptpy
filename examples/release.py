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

    result = camera.eos_run_command("sysConfig")
    if result.ResponseCode == 'OK':
        print("Boot flag enabled.")
    else:
        print("Error running command: %s" % result.ResponseCode)
