#!/usr/bin/python
 
"""
this script installs an interrupt to trigger actions asap
"""

from datetime import datetime
import os
import time
import RPi.GPIO as gpio

# installable via pip
from common import alert, path
  
gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.IN)

while True:
    try:
        channel = gpio.wait_for_edge(11, gpio.RISING)
        if channel is not None:
            alert("DANGER: WATERALARM TRIGGERED")

            with open(os.path.join(path, 'data', 'incidents.dat'), 'a') as f:
                f.write("""{{"time": "{}", "value": {}}}\n""".format(datetime.now(), 1))

        else:
            print("fatal error")
    except Exception as e:
        print(e)        


