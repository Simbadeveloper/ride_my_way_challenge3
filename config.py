import os


class Config(object):
  
    SECRET_KEY = os.environ['APP_SECRET_KEY']


class Testing(Config):
    """
    Configuration for testing environment.
    """

    DEBUG = True
    DB_URI = os.environ['TESTING_DB_URI']
   
class Development(Config):
    """
    Configuration for development environment.
    """

    DEBUG = False
    DB_URI = os.environ['DEVELOPMENT_DB_URI']

configurations = {
    "testing": Testing,
    "development": Development
}
