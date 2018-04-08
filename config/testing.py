# -*- coding: utf-8 -*-

from .config import Configuration


class TestingConfiguration(Configuration):
    DEBUG = True
    TESTING = True


