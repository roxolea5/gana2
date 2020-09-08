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
2. Go to register_blueprints method
3. Import blueprint to register

```
from blueprints.web import web_api
```

4. Register blueprint

```
self.app.register_blueprint(web_api)
```
