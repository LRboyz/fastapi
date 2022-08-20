from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, validator


class BookSerializer(BaseModel):
    id: str
    title: str
    content: str

    author_name: Optional[str]
    created_by: str
    created_at: datetime
    updated_at: datetime


class BookInSerializer(BaseModel):
    title: str
    content: str

    @validator('title')
    def validate_title(cls, v):
        if not v:
            raise ValueError('This field is required')
        if len(v) < 5:
            raise ValueError('Minimum length of title is 5 chars')
        return v

    @validator('content')
    def validate_content(cls, v):
        if not v:
            raise ValueError('This field is required')
        if len(v) < 20:
            raise ValueError(
                'Minimum length of the body of content is 20 chars')
        return v


class BookInPatchSerializer(BaseModel):
    title: Optional[str]
    content: Optional[str]
