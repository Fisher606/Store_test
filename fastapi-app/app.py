from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

app = FastAPI()

# Подключение к базе данных PostgreSQL
connection = psycopg2.connect(
    host="postgres", user="admin", password="admin", dbname="store_db"
)

class Product(BaseModel):
    name: str
    price: float

@app.post("/products/")
async def create_product(product: Product):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (product.name, product.price))
    connection.commit()
    return {"message": "Product added successfully"}

@app.get("/products/")
async def get_products():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
    return {"products": products}
