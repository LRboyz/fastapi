import pydantic
from apps.constants import constants


class BaseSettings(pydantic.BaseSettings):
    class Config:
        env_file = '.env'


class MongoSettings(BaseSettings):
    MONGODB_URI: str = "mongodb://127.0.0.1:27017"
    DATABASENAME: str = "fashionDatabase"
    COLLECTION: str = "fashion"

    class Config(BaseSettings.Config):
        env_prefix = "MONGO_"


# redis配置
REDIS_CONFIG = {
    'default': {
        'host': '127.0.0.1',
        'port': 6379,
        'db': 0,
        'password': '',
        'minsize': 1,
        'maxsize': 5,
        'timeout': 3
    }
}


mongo_settings = MongoSettings()
