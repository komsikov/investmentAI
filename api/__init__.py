__version__ = '0.1'
from flask import Flask
# from flask_debugtoolbar import DebugToolbarExtension

api = Flask('investment')

api.config['SECRET_KEY'] = 'random'
api.debug = True
# toolbar = DebugToolbarExtension(api)

from api.controllers import *
from api.models import *
