from pydantic import BaseModel

class ProductBase(BaseModel):
    id: int
    name: str
    price: int
    category: str

    class Config:
        from_attributes = True
