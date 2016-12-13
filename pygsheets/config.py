import os
import ConfigParser

basedir = os.path.abspath(os.path.dirname(__file__))
# config = ConfigParser.ConfigParser()
# config.read(os.path.abspath(os.environ['CREDENTIALS']))

class Config(object):
    DEBUG = False
    TESTING = False

# class ProductionConfig(Config):
#     DEBUG = False


# class StagingConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True


# class DevelopmentConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True
#     USERNAME = config.get("google","USERNAME")
#     PASSWORD = config.get("google","PASSWORD")


# class TestingConfig(Config):
#     TESTING = True