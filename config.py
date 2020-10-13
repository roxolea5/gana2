import json
import os

path = 'config.prod.json'

if os.path.exists("config.local.json"):
    path = 'config.local.json'

f = open(path, 'r')

config = json.loads(f.read())

try:
    host = os.getenv('db_host')
    if host is None:
        host = config.get("db_host")

    db = os.getenv('db_name')
    if db is None:
        db = config.get("db_name")
    
    user = os.getenv('db_user')
    if user is None:
        user = config.get("db_user")

    pwd = os.getenv('db_password')
    if pwd is None:
        pwd = config.get("db_password")
except Exception as e:
    host = "127.0.0.1"
    db = "sommelier_dev"
    user = "user"
    pwd = "pwd"
    print("***************** ERROR")
    print("***************** APP WILL NOT RUN WITH THE DESIRED VALUES")
    print(str(e))

dbConnString = config.get('DBCONN_STRING_DEV')
dbConnString = dbConnString.replace("{{user}}", user)
dbConnString = dbConnString.replace("{{pwd}}", pwd)
dbConnString = dbConnString.replace("{{host}}", host)
dbConnString = dbConnString.replace("{{db}}", db)

config['DBCONN_STRING_DEV'] = dbConnString
