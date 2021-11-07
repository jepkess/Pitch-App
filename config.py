import os # os module allow the application to interacts with the operating system dependency functionality.

class config:
    SECRET_KEY =os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS=True


class Prodconfig(config):
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