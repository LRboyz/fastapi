from typing import Optional
from xml.dom.minidom import Document
from umongo import Document, fields, EmbeddedDocument
from apps.core.database.db import instance, db
from bson import ObjectId
from datetime import datetime


@instance.register
class Book(Document):
    title = fields.StrField()
    content = fields.StrField()

    author_name = fields.StrField(allow_none=True, default='')
    # created_by = fields.ReferenceField(User)
    created_at = fields.DateTimeField(default=datetime.now)
    updated_at = fields.DateTimeField(default=datetime.now)

    class Meta:
        collection = db.post

    @classmethod
    async def get(cls, id: str) -> Optional['Book']:
        if not ObjectId.is_valid(id):
            return None

        return await cls.find_one({'_id': ObjectId(id)})
