from sqlalchemy_serializer import SerializerMixin
from extensions.db import DB
db = DB.db
DB_ENGINE = 'dev'


class Rancho(db.Model, SerializerMixin):
    __bind_key__ = DB_ENGINE
    __tablename__ = 'cat_ranchos'
    __table_args__ = {
        'autoload': True,
        'autoload_with': DB.engines[DB_ENGINE].engine
    }

    def __init__(self):
        pass
