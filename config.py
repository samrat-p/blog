# application configurations

import os

# current directory of the project
basedir = os.path.abspath(os.path.dirname(__file__))

# common configurations
class Config:
    SECRET_KEY = "secret_key_goes_here"
    # more configurations goes hereß

    @staticmethod
    def init_app(app):
        pass

# development configurations
class DevelopmentConfig(Config):
    pass

# testing configurations
class TestingConfig(Config):
    pass

# production configurations
class ProductionConfig(Config):
    pass

# available configuration types
config = {
    'default'       :   DevelopmentConfig,
    'development'   :   DevelopmentConfig,
    'testing'       :   TestingConfig,
    'production'    :   ProductionConfig
}