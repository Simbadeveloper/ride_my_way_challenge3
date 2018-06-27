import os
import psycopg2

#connecting to the database
con = psycopg2.connect(os.environ['DEV_DB_URI'])

class Config(object):
    """ Base configuration. """

    SECRET_KEY = os.environ['APP_SECRET_KEY']


class TestingConfig(Config):
    """  Testing environment configuration  """

    DEBUG = True
    
    
class DevelopmentConfig(Config):
    """  Development environment configuration.  """

    DEBUG = False
        
configurations = {
    "testing": TestingConfig,
    "development": DevelopmentConfig
}
