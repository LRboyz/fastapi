import os


# 项目基准路径（house_rental/house_rental）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 项目静态目录（演示可以用）
STATIC_FILE_DIR = os.path.join(os.path.dirname(BASE_DIR), 'resource/')

# 放到模块下面防止循环依赖
# 数据库配置
from .db_config import REDIS_CONFIG
from .db_config import mongo_settings

# 日志配置
from .logging_config import LOGGING_CONF