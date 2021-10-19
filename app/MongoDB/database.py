import pymongo
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
import motor.motor_asyncio

client = pymongo.MongoClient()
MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
mongodb = client.users
users_collection = mongodb.get_collection("users")


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid object id")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class UserModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "User",
                "email": "user@example.com",
            }
        }
