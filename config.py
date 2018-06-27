import os


class Config(object):
  
    SECRET_KEY = os.environ['APP_SECRET_KEY']


class Testing(Config):
    """
    Configuration for testing environment.
    """

    DEBUG = True
 
   
class Development(Config):
    """
    Configuration for development environment.
    """

    DEBUG = False
    

configurations = {
    "testing": Testing,
    "development": Development
}
