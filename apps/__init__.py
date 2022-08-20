import logging
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from apps.core import settings
from apps import constants
from apps.api.v1.modules import router
from loguru import logger
from fastapi.middleware.cors import CORSMiddleware
from pymongo.collection import Collection
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI(
    title="FastAPI",
    description='',
    version='v1.0.0',
    debug=True,
    servers=''
)

__all__ = ("client", 'collection')

# 挂载静态文件方便演示也可单独部署前端
app.mount("/static", StaticFiles(directory=settings.STATIC_FILE_DIR), name="static")


@app.on_event("startup")
async def startup_event():
    """项目启动时启动环境"""

    """配置项目日志器"""
    setup_logging()

    """加载路由"""
    app.include_router(router, prefix='/api/v1')
    # app.include_router(hello_router)

    """注册中间件"""
    await register_middlewares(app)

    """创建全局异常处理器"""

    """数据库初始化"""
    await db_init()


@app.on_event("shutdown")
def shutdown_db_client():
    logging.info("close mongodb connection....")
    app.mongodb_client.close()
    logging.info("connection to mongodb has been closed!")


def setup_logging(logging_conf=settings.LOGGING_CONF):
    """
    配置项目日志信息
    :param logging_conf: 项目日志配置
    :return:
    """
    for log_handler, log_conf in logging_conf.items():
        log_file = log_conf.pop('file', None)
        logger.add(log_file, **log_conf)


async def create_global_exception_handler():
    """创建全局异常处理器"""


async def register_middlewares(_app: FastAPI):
    """注册中间件"""
    middleware_list = []
    for middleware in middleware_list:
        _app.add_middleware(middleware)

      # 设置跨域中间件
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=constants.ALLOR_ORIGIN,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# 初始化Redis(暂时不用)
# async def init_redis(_app: FastAPI, redis_conf):
#     pass


async def db_init():
    """ 数据库初始化 """
    from apps.core.database.db import database
    logging.info("connect to database....")
    database.client = AsyncIOMotorClient(
        str(settings.mongo_settings.MONGODB_URI))
    logging.info("Connected to database!")
