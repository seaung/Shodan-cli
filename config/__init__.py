# -*- coding: utf-8 -*-
import os


def load_config():

    mode = os.environ.get('MODE')

    try:
        if mode == 'PRODUCTION':
            from .production import ProductConfiguration
            return ProductConfiguration
        elif mode == 'TESTING':
            from .testing import TestingConfiguration
            return TestingConfiguration
        else:
            from .devlopment import DevlopmentConfiguration
            return DevlopmentConfiguration
    except ImportError, e:
        from .config import Config
        return Config

