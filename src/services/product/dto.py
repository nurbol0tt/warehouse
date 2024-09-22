from pydantic import BaseModel


class Product(BaseModel):
    title: str
    description: str
    price: float
    total: float

