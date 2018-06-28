import os


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
