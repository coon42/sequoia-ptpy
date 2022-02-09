#!/usr/bin/env python
import ptpy

camera = ptpy.PTPy()
info = camera.get_device_info()

print(info)
print('----------------')
ops = info['OperationsSupported']

ops_int = [hex(x) for x in ops if isinstance(x, int)]
ops_str = [x for x in ops if isinstance(x, str)]

ops_int.sort()
ops_str.sort()

print(ops_int)
print('')
print(ops_str)

