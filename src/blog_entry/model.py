from pydantic import BaseModel, Field
from typing import Optional, List


class BlogEntrySchema(BaseModel):
    id: Optional[int]
    title: str = Field(...)
    tags: List[str] = Field(...)

    class Config:
        schema_extra = {"example": {"title": "Pet Cemetery", "tags": ["Books", "Test"]}}


class UpdateBlogEntrySchema(BaseModel):
    title: Optional[str]
    tags: Optional[List[str]]

    class Config:
        schema_extra = {"example": {"title": "It", "tags": ["Books", "Test"]}}
