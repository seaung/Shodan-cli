# -*- coding: utf-8 -*-
from .config import Configuration


class DevlopmentConfiguraion(Configuration):

    DEBUG = True

    SQLALCHEMY_DATBASE_URI = '' 
