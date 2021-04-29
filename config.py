from environs import Env

env = Env()
env.read_env()

DB_BASE_URI = "sqlite:///{}.db"


class Config:
    db_name = ""
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_name}.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False
    PROPAGATE_EXCEPTIONS = True
    JWT_SECRET_KEY = env.str("SECRET_KEY")
    JWT_BLOCKLIST_ENABLED = True
    JWT_BLOCKLIST_TOKEN_CHECKS = ["access", "refresh"]


class DevelopmentConfig(Config):
    db_name = env.str("DB_NAME_DEV")


class TestConfig(Config):
    db_name = env.str("DB_NAME_TEST")
    TESTING = True


config_selector = {
    "development": DevelopmentConfig,
    "test": TestConfig,
}
