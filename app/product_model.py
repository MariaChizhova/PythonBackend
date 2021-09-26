from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Product(BaseModel):
    name: str
    calories: float
    proteins: float
    fats: float
    carbohydrates: float
    date: datetime
    description: Optional[str] = None
