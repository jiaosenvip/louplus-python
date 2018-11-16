from importlib import import_module

from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
session = Session()
migrate = Migrate()


def init(app):
    global db, session, migrate

    db = SQLAlchemy(app)
    session = db.session
    migrate = Migrate(app, db)

    import_module('.models', __package__)