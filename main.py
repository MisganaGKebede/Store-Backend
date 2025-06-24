from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.session import engine, Base
from routers.product import router as product_router

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # use ["http://localhost:5177"] for strict CORS
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

# Register product route
app.include_router(product_router, prefix="/products", tags=["Products"])


@app.get("/")
def read_root():
    return {"message": "Ecolora Backend is running 🚀"}
