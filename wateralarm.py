#!/usr/bin/python
 
"""
 this script is called every minute by a cronjob and writes
 data to a buffer, which can be read by waterserver.py
 to prevent file access violations we lock the buffer file
 before reading and writing, such that only one script may
 access the file
"""

from datetime import datetime
import sys
import os
import time
import RPi.GPIO as gpio

# installable via pip
from filelock import Timeout, FileLock

# common source
from common import alert, path, max_buffer_size

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.IN)
filename = os.path.join(path, 'data', 'buffer.dat')

with FileLock(filename + '.lock', timeout=2):
    
    # try to read old dataset, if it doesn't exist
    # initialize an empty buffer
    try:
        with open(filename, 'rt') as f:
            data = f.readlines()
    except:
        data = []
        
    wateralarm = 1-gpio.input(11)

    if wateralarm:
        alert('DANGER: WATERALARM ACTIVE!')

    with open(filename, 'wt') as f:
        f.writelines(data[-(max_buffer_size-1):])
        f.write("""{{"time": "{}", "value": {}}}\n""".format(datetime.now().isoformat(), wateralarm))
