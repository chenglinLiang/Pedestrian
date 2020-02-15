import os


basedir = os.getcwd()

class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')


class Development(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL')


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('PRO_DATABASE_URL')


config = {
    'development': Development,
    'production': ProductionConfig
}
