from db.session import SessionLocal
from models.product import Product

# Replace with your actual image URLs
image_urls = {
    "Organic Bananas": "https://example.com/images/bananas.jpg",
    "Organic Strawberries": "https://example.com/images/strawberries.jpg",
    "Organic Carrots": "https://example.com/images/carrots.jpg",
    "Organic Avocados": "https://example.com/images/avocados.jpg",
    "Organic Eggs": "https://example.com/images/eggs.jpg",
    "Organic Almond Milk": "https://example.com/images/almondmilk.jpg",
    "Organic Spinach": "https://example.com/images/spinach.jpg",
    "Organic Apples": "https://example.com/images/apples.jpg"
}

db = SessionLocal()

for name, url in image_urls.items():
    product = db.query(Product).filter(Product.name == name).first()
    if product:
        product.image = url
        db.add(product)

db.commit()
db.close()
print("✅ Product images updated.")
