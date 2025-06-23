from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    image: str

class ProductCreate(ProductBase):
    pass

# ✅ This is what FastAPI is looking for
class ProductOut(ProductBase):
    id: int

    class Config:
        from_attributes = True  # use this if you're on Pydantic v2
