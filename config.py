import json
import os

path = 'config.prod.json'

if os.path.exists("config.local.json"):
    path = 'config.local.json'

f = open(path, 'r')

config = json.loads(f.read())
