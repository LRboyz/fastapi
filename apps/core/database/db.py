from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from umongo.frameworks import MotorAsyncIOInstance

from apps.core import settings


class DataBase:
    client: AsyncIOMotorClient = None


database = DataBase()


def get_database() -> AsyncIOMotorDatabase:
    if database.client:
        return database.client[settings.mongo_settings.MONGODB_URI]
    return AsyncIOMotorClient(settings.mongo_settings.MONGODB_URI)[settings.mongo_settings.DATABASENAME]


def get_client() -> AsyncIOMotorClient:
    if not database.client:
        return AsyncIOMotorClient(settings.mongo_settings.MONGODB_URI)
    return database.client


db = get_database()
instance = MotorAsyncIOInstance(db)
