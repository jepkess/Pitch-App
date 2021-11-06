from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options


bootstrap=Bootstrap()

def create_app(config_name):
  app=Flask(__name__)


  #creating the app configurations
  app.config.from_object(config_options[config_name])

  #Initializing the flask-extensions
  bootstrap.init_app(app) #calling the init_app on the extension to complete the initialization.

  #Registering the Blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  return app

  
    

