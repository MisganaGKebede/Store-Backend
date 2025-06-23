from db.session import SessionLocal, engine
from models.product import Product
from db.session import Base

# Create the table if not exists
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Clear old data
db.query(Product).delete()

# ✅ 8 Organic Food Products
products = [
    Product(
        name="Organic Bananas",
        description="Fresh organic bananas from local farms",
        price=1.99,
        image="https://cdn.shopify.com/s/files/1/0499/2089/5831/products/organic-bananas.jpg"
    ),
    Product(
        name="Organic Strawberries",
        description="Sweet and juicy organic strawberries",
        price=3.99,
        image="https://cdn.shopify.com/s/files/1/0583/9147/0873/products/strawberries.jpg"
    ),
    Product(
        name="Organic Carrots",
        description="Crunchy organic carrots perfect for snacking",
        price=2.49,
        image="https://cdn.shopify.com/s/files/1/0572/1286/9832/products/OrganicCarrots.jpg"
    ),
    Product(
        name="Organic Avocados",
        description="Creamy and healthy organic avocados",
        price=4.99,
        image="https://cdn.shopify.com/s/files/1/0583/9147/0873/products/organic-avocados.jpg"
    ),
    Product(
        name="Organic Eggs",
        description="Free-range organic eggs (12 count)",
        price=5.49,
        image="https://cdn.shopify.com/s/files/1/0583/9147/0873/products/organic-eggs.jpg"
    ),
    Product(
        name="Organic Almond Milk",
        description="Unsweetened organic almond milk",
        price=3.29,
        image="https://cdn.shopify.com/s/files/1/0583/9147/0873/products/almond-milk.jpg"
    ),
    Product(
        name="Organic Spinach",
        description="Fresh organic baby spinach",
        price=2.79,
        image="https://cdn.shopify.com/s/files/1/0572/1286/9832/products/spinach.jpg"
    ),
    Product(
        name="Organic Apples",
        description="Crisp organic red apples (per lb)",
        price=2.99,
        image="https://cdn.shopify.com/s/files/1/0583/9147/0873/products/apples.jpg"
    ),
]

db.add_all(products)
db.commit()

print("✅ Seeded 8 organic products successfully.")
