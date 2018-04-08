# -*- coding: utf-8 -*-
import os


class ProductConfiguration(object):

    DEBUG = False

    TESTING = False

    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__). '..'))


    SQLALCHEMY_DATABASE_URI = ''


