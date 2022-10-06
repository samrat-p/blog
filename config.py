# application configurations

import os

# current directory of the project
basedir = os.path.abspath(os.path.dirname(__file__))

# common configurations
class Config:
    SECRET_KEY = "d35c499d686fe9e03ffc4c6f8636e7c21b08ad9211a9e8255d0c50f4465bc454"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # client information provided by authorization server
    CLIENT_ID = "client_id_goes_here"
    CLIENT_SECRET = "client_secret_goes_here"

    @staticmethod
    def init_app(app):
        pass

# development configurations
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app/data/database.db')
    SQLALCHEMY_ECHO = True
    DEBUG = True
    
# testing configurations
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app/data/database.db')
    SQLALCHEMY_ECHO = True
    TESTING = True

# production configurations
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '/app/db/data.db')
    SQLALCHEMY_ECHO = False

# available configuration types
config = {
    'default'       :   DevelopmentConfig,
    'development'   :   DevelopmentConfig,
    'testing'       :   TestingConfig,
    'production'    :   ProductionConfig
}
