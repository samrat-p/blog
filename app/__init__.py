# application instance

from flask import Flask
from config import config
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name = 'default'):
    ''' Creates an application instances and return it to the caller
    param   :   config_name = an configuration type defined in config.py
    return  :   application instance '''

    app = Flask(__name__)                               # application instance obeject
    app.config.from_object(config[config_name])         # configure with defined config-type
    config[config_name].init_app(app)                   # initialization application instance

    moment.init_app(app)                                # register flask_moment
    db.init_app(app)                                    # register flask_sqlalchemy
    login_manager.init_app(app)                         # register flask_login

    from .auth import auth_blueprint                    # registering blurprints to the instance
    from .main import main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    # other configuration binding goes here
    
    return app
