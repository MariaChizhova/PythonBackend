from pydantic import BaseModel
from bson import ObjectId


class User(BaseModel):
    _id: ObjectId
    name: str
    email: str
    username: str

