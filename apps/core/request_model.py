from typing import List, Optional
from pydantic import BaseModel, Field


class ListPageRequestModel(BaseModel):
    """分页请求模型"""
    offset: int = Field(default=0, ge=0, description="分页偏移量")
    limit:  int = Field(default=10, gt=0, description='每页显示数量')
    query_params: Optional[dict] = Field(default={}, description='查询参数')
    orderings:    Optional[List[str]] = Field(default=None, description='排序字段')
