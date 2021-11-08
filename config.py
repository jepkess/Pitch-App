import os # os module allow the application to interacts with the operating system dependency functionality.

class config:
    SECRET_KEY =os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    UPLOADED_PHOTOS_SET='app/static/photos'

    #Email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class Prodconfig(config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postges://"):
        SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI.replace("postgres://","postgesql://", 1)
    """
    configuring the application on the production mode.
    """ 
    pass

class Devconfig(config):
    DEBUG=True
#a dictionary that help us access different configuration option classes.
config_options={
    'development':Devconfig,
    'production': Prodconfig
}    