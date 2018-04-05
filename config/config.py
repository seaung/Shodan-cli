class Configuration(object):
    DEGUB = False
    TESTING = False
    DATABASE_URL = ''


class DevlopmentConfiguration(Configuration):
    DEBUG = True
    DATABASE_URI = ''


class ProductConfiguration(Configuration):
    DATABASE_URI = ''


class TestingConfiguration(Configuration):
    TESTING = False

