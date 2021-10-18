from app.product_model import Product
from app.calculations import Products
import datetime
from graphene import Schema
from fastapi import FastAPI, HTTPException, Response, Depends
from starlette.graphql import GraphQLApp
from app.query import Query
from graphql.execution.executors.asyncio import AsyncioExecutor
from app.database import SessionLocal, engine
from sqlalchemy.orm import Session
from app import requests, models

app = FastAPI()
products = Products()
models.Base.metadata.create_all(bind=engine)

app.add_route("/graphql", GraphQLApp(schema=Schema(query=Query), executor_class=AsyncioExecutor))


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/add_user/{user}')
async def add_user(email: str, password: str, response: Response, db: Session = Depends(get_db)):
    if requests.get_user_by_email(db, email):
        response.status_code = 409
        return HTTPException(status_code=409, detail="User with this email exists")
    requests.add_user(db=db, email=email, password=password)
    return True


@app.get('/get_users/')
async def get_users(db: Session = Depends(get_db)):
    return requests.get_users(db=db)


@app.get('/get_user_by_id/{user_id}')
async def get_users_by_id(user_id: int, db: Session = Depends(get_db)):
    return requests.get_user_by_id(user_id=user_id, db=db)


@app.get('/get_user_by_email/{email}')
async def get_users(email: str, db: Session = Depends(get_db)):
    return requests.get_user_by_email(email=email, db=db)


@app.post('/add_product/{product}')
async def add_product(name: str, calories: float, proteins: float, fats: float, carbohydrates: float,
                      description: str, owner_id: int, db: Session = Depends(get_db)):
    requests.add_user_product(name=name, calories=calories, proteins=proteins, fats=fats, carbohydrates=carbohydrates,
                              description=description, owner_id=owner_id, db=db)
    return True


@app.get('/get_products/')
async def get_products(db: Session = Depends(get_db)):
    return requests.get_products(db=db)


@app.get('/get_products_by_id/{owner_id}')
async def get_users(owner_id: int, db: Session = Depends(get_db)):
    return requests.get_user_products_by_id(owner_id=owner_id, db=db)


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
