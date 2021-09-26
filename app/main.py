from fastapi import FastAPI
from app.product_model import Product
from app.calculations import Products
import datetime

app = FastAPI()
products = Products()


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.post("/products/")
async def create_item(product: Product):
    return products.add_item(product)


@app.get("/tracker/{products_id}")
def get_product_id(product_id):
    return {"product_id": product_id}


@app.get("/calculate/calories/")
def calculate_calories():
    return products.calculate("calories")


@app.get("/calculate/proteins/")
def calculate_proteins():
    return products.calculate("proteins")


@app.get("/calculate/fats/")
def calculate_fats():
    return products.calculate("fats")


@app.get("/calculate/carbohydrates/")
def calculate_carbohydrates():
    return products.calculate("carbohydrates")


@app.get("/total/{year}/{month}/{day}")
def total_by_day(year: int, month: int, day: int):
    return products.total_by_date(datetime.date(year, month, day))


@app.get("/total/")
def total():
    return products.total()


@app.get("/calculate_mean/{number}")
def calculate_mean(number: int):
    # last 'number' days
    today = datetime.date.today()
    first_day = today - datetime.timedelta(days=number)
    return products.mean_between_days(first_day, today, number)
