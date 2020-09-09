# gana2

## Flask Workflow

### Creating blueprint

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

### Registering blueprint

1. Go to ./webserver.py
2. Go to register_blueprints function
3. Import blueprint to register

```
from blueprints.web import web_api
```

4. Register blueprint

```
self.app.register_blueprint(web_api)
```

### Registering model

#### Creating DB Extension

1. Go to config.local.json
2. Modify DB Connection Strings

```
"DATABASE_CONNECTION_STRING": "mysql+pymysql://YOUR_USER:YOUR_PASSWORD@YOUR_IP/DB_NAME",
  "DBCONN_STRING_DEV": "mysql+pymysql://YOUR_USER:YOUR_PASSWORD@YOUR_IP/DB_NAME",
  "DBCONN_STRING_PROD": "mysql+pymysql://YOUR_USER:YOUR_PASSWORD@YOUR_IP/DB_NAME"
```

3. Create "extensions" folder
4. Generate db.py for DB environment set up

#### Creating Model

1. Create "./models/" folder
2. Add Raza model

```
from sqlalchemy_serializer import SerializerMixin
from extensions.db import DB
db = DB.db
DB_ENGINE = 'dev'


class Raza(db.Model, SerializerMixin):
    __bind_key__ = DB_ENGINE
    __tablename__ = 'cat_razas'
    __table_args__ = {
        'autoload': True,
        'autoload_with': DB.engines[DB_ENGINE].engine
    }

    def __init__(self):
        pass
```

#### Creating Controller

1. Create "./controllers/" folder
2. Create controller class on razas.py and import the model in it.

```
from models.cat_razas import Raza
```

3. Add getall static method

```

    def get_all():
        return Raza.query.filter().all()
```

#### Register DB Extension

1. Go to ./webserver.py and register it on register_extensions function

```
from extensions.db import DB
DB.init_app(self.app)
```

current branch: lotes
