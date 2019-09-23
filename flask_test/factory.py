from flask import Flask
from .database import DATABASE
from .views import register as register_views
from flask_sqlalchemy import SQLAlchemy

def application(daba_url, name =__package__, database = DATABASE):
    application = Flask(name)
    application.config['SQLALCHEMY_DATABASE_URI'] = daba_url
    register_views(application)
    application.database = database
    application.database.init_app(application) # SQLAlchemy(app=application)
    return application