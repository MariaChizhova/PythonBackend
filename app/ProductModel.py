from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Product(BaseModel):
    name: str
    calories: float
    date: datetime
    description: Optional[str] = None
