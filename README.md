# gana2

## Running the app

Make sure you have the ENVIRONMENT variables for DEVELOPMENT mode properly configured:

```
export FLASK_ENV=development
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
.
.
.
self.app.register_blueprint(razas_api)
```

## Technical Workflow for a new endpoint.

```
- Add the class on migration.py
- Do the migration process
- Create the model
- Create the controller and, import the model
- Create the blueprint.
- Register you blueprint into webserver.py at register_blueprints method.
```
