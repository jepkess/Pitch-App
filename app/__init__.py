from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_sqlalchemy import SQLAlchemy #SQLAlchemy is a mapper that connect the application to the database.
from flask_login import LoginManager
import os
from flask_mail import Mail



login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login' 
bootstrap=Bootstrap()
db=SQLAlchemy()
photos=UploadSet('photos',IMAGES)
mail=Mail()



def create_app(config_name):
  app=Flask(__name__)

  #creating the app configurations
  app.config.from_object(config_options[config_name])

  #configure the uploadset
  # configure_uploads(app,photos)
  app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()

  #Initializing the flask-extensions
  bootstrap.init_app(app) #calling the init_app on the extension to complete the initialization.
  db.init_app(app)
  login_manager.init_app(app)
  mail.init_app(app)

  #Registering the main Blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)


  #Registering the auth Blueprint
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
  

   
  return app

  
    

