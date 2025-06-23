from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import SessionLocal
from models.product import Product

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to fetch all products
@router.get("/")
def read_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

# Route to insert initial products
@router.post("/init-products")
def init_products(db: Session = Depends(get_db)):
    products = [
        {
            "name": "Organic Bananas",
            "description": "Fresh organic bananas from local farms",
            "price": 1.99,
            "image": "/images/bananas.jpg"
        },
        {
            "name": "Organic Strawberries",
            "description": "Sweet and juicy organic strawberries",
            "price": 3.99,
            "image": "/images/strawberries.jpg"
        },
        {
            "name": "Organic Carrots",
            "description": "Crunchy organic carrots perfect for snacking",
            "price": 2.49,
            "image": "/images/carrots.jpg"
        },
        {
            "name": "Organic Avocados",
            "description": "Creamy and healthy organic avocados",
            "price": 4.99,
            "image": "/images/avocados.jpg"
        },
        {
            "name": "Organic Eggs",
            "description": "Free-range organic eggs (12 count)",
            "price": 5.49,
            "image": "/images/eggs.jpg"
        },
        {
            "name": "Organic Almond Milk",
            "description": "Unsweetened organic almond milk",
            "price": 3.29,
            "image": "/images/milks.jpg"
        },
        {
            "name": "Organic Spinach",
            "description": "Fresh organic baby spinach",
            "price": 2.79,
            "image": "/images/spinach.jpg"
        },
        {
            "name": "Organic Apples",
            "description": "Crisp organic red apples (per lb)",
            "price": 2.99,
            "image": "/images/apples.jpg"
        },
    ]

    for p in products:
        existing = db.query(Product).filter_by(name=p["name"]).first()
        if not existing:
            db.add(Product(**p))
    db.commit()
    return {"message": "Products initialized successfully."}

# ✅ New route to fix/update product image paths
@router.post("/fix-images")
def fix_images(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    for product in products:
        name = product.name.lower().replace("organic ", "").replace(" ", "_")
        product.image = f"/images/{name}.jpg"
    db.commit()
    return {"message": "✅ Product images updated to local /images path"}
