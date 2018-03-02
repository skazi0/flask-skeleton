class BaseConfig(object):
    SECRET_KEY = 'my_precious'
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_DATABASE_URI = 'mysql://user:pass@localhost/dbname'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
