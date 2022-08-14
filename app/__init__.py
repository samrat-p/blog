# application instance

from flask import Flask
from config import config
from flask_moment import Moment

moment = Moment()

def create_app(config_name):
    ''' Creates an application instances and return it to the caller
    param   :   config_name = an configuration type defined in config.py
    return  :   application instance '''

    app = Flask(__name__)                               # application instance obeject
    app.config.from_object(config[config_name])         # configure with defined config-type
    config[config_name].init_app(app)                   # initialization application instance

    moment.init_app(app)                                # register flask_moment

    from .auth import authentication_blueprint          # registering blurprints to the instance
    from .general import general_blueprint
    app.register_blueprint(authentication_blueprint)
    app.register_blueprint(general_blueprint)

    # other configuration binding goes here
    
    return app
