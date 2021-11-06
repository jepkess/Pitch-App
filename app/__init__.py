from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options


bootstrap=Bootstrap()

def create_app(config_name):
  app=Flask(__name__)


  #creating the app configurations
  app.config.from_object(config_options[config_name])

  #Initializing the flask-extensions
  bootstrap.init_app(app)
  
from app.main import views

