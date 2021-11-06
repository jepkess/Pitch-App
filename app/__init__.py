from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy #SQLAlchemy is a mapper that connect the application to the database.


bootstrap=Bootstrap()
db=SQLAlchemy()

def create_app(config_name):
  app=Flask(__name__)
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

  


  #creating the app configurations
  app.config.from_object(config_options[config_name])

  #Initializing the flask-extensions
  bootstrap.init_app(app) #calling the init_app on the extension to complete the initialization.
  db.init_app(app)

  #Registering the Blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  return app

  
    

