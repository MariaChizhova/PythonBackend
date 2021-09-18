from fastapi import FastAPI, HTTPException
from ProductModel import Product

app = FastAPI()
products = dict()


def check_name_correctness(name: str):
    if name == "":
        raise HTTPException(status_code=400, detail="Invalid name")


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.post("/products/")
async def create_item(product: Product):
    check_name_correctness(product.name)
    date = product.date.date()
    if date not in products:
        products[date] = []
    products[date].append(product.calories)
    return product


@app.get("/tracker/{products_id}")
def get_product_id(product_id):
    return {"product_id": product_id}


@app.get("/calculate/")
def calculate():
    result = []
    for date in products:
        result.append({date: sum(products[date])})
    return result



