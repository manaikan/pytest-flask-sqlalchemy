import sqlalchemy
import flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

DATABASE = SQLAlchemy()
# from .config import DATABASE_URL
# engine = sqlalchemy.create_engine(DATABASE_URL) # Commenting this makes little difference to the tests