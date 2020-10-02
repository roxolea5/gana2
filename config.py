import json
import os

path = 'config.prod.json'

if os.path.exists("config.local.json"):
    path = 'config.local.json'

f = open(path, 'r')

host = os.getenv('gana2_host')
db = os.getenv('gana2_db')
user = os.getenv('gana2_db_user')
pwd = os.getenv('gana2_db_pwd')


config = json.loads(f.read())
dbConnString = config.get('DBCONN_STRING_DEV')
dbConnString = dbConnString.replace("{{user}}", user)
dbConnString = dbConnString.replace("{{pwd}}", pwd)
dbConnString = dbConnString.replace("{{host}}", host)
dbConnString = dbConnString.replace("{{db}}", db)

config['DBCONN_STRING_DEV'] = dbConnString
