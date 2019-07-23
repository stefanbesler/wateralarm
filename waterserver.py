#!/usr/bin/python

"""
webserver that can stream data to clients. A buffer file is read and
checked for changes. If there are any changes since the last time the
file was read, all modifications are sent to the clients
"""

import json
import time
import os
from datetime import datetime

# installable via pip
from flask import Flask, Response, render_template
from filelock import Timeout, FileLock

# common source
from common import path

application = Flask(__name__, template_folder='template')

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/chart-data')
def chart_data():
    def read_data():
        def read_timestamp(json_line): 
            date = datetime.strptime(json.loads(json_line)["time"], "%Y-%m-%dT%H:%M:%S.%f") 
            return date

        timestamp = None
        while True:
            with FileLock(os.path.join(path, 'data', 'buffer.dat.lock'), timeout=2):
                with open(os.path.join(path, 'data', 'buffer.dat'), 'rt') as f:
                    data = f.readlines()
                    for d in data:
                        if timestamp is None or read_timestamp(d) > timestamp:
                            yield f"data:{d}\n\n"
                         
                    timestamp = read_timestamp(data[-1]) 

            time.sleep(1)

    return Response(read_data(), mimetype='text/event-stream')

if __name__ == '__main__':
    application.run(host='192.168.178.107', debug=True, threaded=True)
