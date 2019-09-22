import sqlalchemy
import flask_sqlalchemy
from .config import DATABASE_URL

db = flask_sqlalchemy.SQLAlchemy()
engine = sqlalchemy.create_engine(DATABASE_URL)