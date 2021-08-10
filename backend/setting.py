class Config:
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = 'Super_Secret_JWT_KEY'
    JWT_ACCESS_TOKEN_EXPIRES = False


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'

# class ProductionConfig(Config):


class TestingConfig(Config):
    TESTING = True
