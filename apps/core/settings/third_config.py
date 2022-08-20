# 项目基准路径（house_rental/house_rental）
from .logging_config import LOGGING_CONF
from .db_config import REDIS_CONFIG
from .db_config import MYSQL_CONFIG
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
