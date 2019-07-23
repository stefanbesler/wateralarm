import os
import json
import pushover

max_buffer_size = 100
path = os.path.abspath(os.path.dirname(__file__))
cfg_filename = os.path.join(path, '.config')


with open(cfg_filename) as f:
    cfg =  json.load(f)

def alert(message, title="wateralarm"):
    pushover.Client(cfg["user"], api_token=cfg["api_token"]).send_message(message, title=title)
    print(message)

