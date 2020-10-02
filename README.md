# gana2

## Running the app

Whenever the environment you want to run, just have to set the flask env variable. For developing mode use:

```
export FLASK_ENV=development
```

For production mode use:

```
export FLASK_ENV=PRODUCTION
```

Make sure you have the ENVIRONMENT variables each case mode properly configured:

```
export gana2_host=127.0.0.1
export gana2_db=DB
export gana2_db_user=DB_USER
export gana2_db_pwd=DB_USER_PWD
```

### Start services Before runing

```
sudo service mysql start
```

### Activate venv and install requirements

```
source venv/bin/activate
pip3 install -r requirements.txt
```

App will runs by typing:

```
make run
```

## Flask Workflow

### Creating single Blueprint

1. Add blueprint file to blueprints folder(web.py)
2. Create blueprint object instance.

```
web_api = Blueprint('web_api', __name__)
```

3. Create endpoint

```
@web_api.route('/')
def index():
    return "Hi"
```

### Flask WorkFlow: Adding a new endpoint

#### 1. Create the Model

Add Raza model to "./models/" folder

```
from sqlalchemy_serializer import SerializerMixin
from extensions.db import DB
db = DB.db


class Raza(db.Model, SerializerMixin):
__tablename__ = 'cat_razas'

    def __init__(self):
        pass
```

#### 2. The Controller

Import the model into the controller file.

```
from models.cat_razas import Raza
```

Add `getall` static method

```
    def get_all():
        return Raza.query.filter().all()
```

#### 3. The BluePrint

Go to ./webserver.py and check the `register_blueprints` method.

Import the blueprint to register and register it

```
from blueprints.razas import razas_api

self.app.register_blueprint(razas_api)
```

## Migrations:

For the first time, run the following on your DBMS, for this case MySQL Workbench

```
DROP DATABASE IF EXISTS `rancho_dev`;
CREATE DATABASE `rancho_dev` /*!40100 COLLATE 'utf8_spanish_ci' */
```

Run the migrations. If this is the very first time, and there is no "migrations" folder on the project, then type:

```
python3 migrations.py db init
```

Whenever you need a change on db, go to ./migrations.py file in order to add or remove features. Then type:

```
python3 migrations.py db migrate
python3 migrations.py db upgrade
```

## Database Backup

While running MySQL 5.7 version on Server and MySQL 8.0 on Client. And try remote databse backup from Client, with this command:

```
mysqldump -h [host] -u[user_name] -p [database] > [dump_file].sql
```

This error appears:

```
Unknown table ‘COLUMN_STATISTICS’ in information_schema (1109)
```

This is due to a new flag that is enabled by default in mysqldump 8. You can disable it by adding:

```
-–column-statistics=0.
```

The command will be something like:

```
mysqldump --column-statistics=0 -h 192.168.56.101 -uroxana -p rancho_dev > rancho_dev_20200917.sql
```

You have to enter your password and the dump file will be created.

## Technical Workflow for a new endpoint.

```
- Add the class on migration.py
- Do the migration process
- Create the model
- Create the controller and, import the model
- Create the blueprint.
- Register you blueprint into webserver.py at register_blueprints method.
```

## Working with Docker

Install docker before next steps.

### Create Dockerfile on project

1. I am going to use Alpine Linux

```
FROM alpine:3.10
```

2. Install python3 and pip

```
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip
```

3. Following instruction will define a directory where image will work

```
WORKDIR /g2app
```

4. Copy project´s content on last directory with

```
COPY . /g2app
```

5. Install requirements.txt

```
RUN pip3 --no-cache-dir install -r requirements.txt
```

6. Indicate which file will be executed with:

```
CMD ["python3", "webserver.py"]
```

### On Terminal

1. To create docker image use `docker build`command followed by `-t`and `image_name` and add all projects content with `.`

```
docker build -t gana2app .
```

2. Check image has been created with

```
docker images
```

3. You can also seen the image content with

```
docker run -it gana2app /bin/sh
```

4. Now to run image we need to set environment variables on `docker run` command. -it will run interactive mode and --publish define image port and local project port at the end is our image name

```
docker run -e gana2_host=host_ip -e gana2_db=db_name -e gana2_db_user=user_name -e gana2_db_pwd=user_password -e FLASK_ENV=development -it --publish 4000:5000 gana2app
```

current branch: docker-compose-try
