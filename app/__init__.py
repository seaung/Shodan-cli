#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from flask import Flask
from config import load_config
from .extends import db
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if project_path not in sys.path:
    sys.path.insert(0, project_path)

try:
	reload(sys)
	sys.setdefaultencoding = 'utf-8'
except NameError:
	try:
	    from importlib import reload
	    reload(sys)
	    sys.setdefaultencoding = 'utf-8'
	except ImportError:
		from imp import reload
		reload(sys)
		sys.setdefaultencoding = 'utf-8'



def create_app():
    app = Flask(__name__)

    config = load_config()

    app.config.from_object(config)
    db.init_app(app)

    return app
