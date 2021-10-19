from app.SQLite import models
from sqlalchemy.orm import Session


def add_user(db: Session, name: str, email: str, password: str):
    user = models.User(name=name, email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def add_user_product(db: Session, name: str, calories: float, proteins: float, fats: float, carbohydrates: float,
                     description: str, owner_id: int):
    product = models.Product(name=name, calories=calories, proteins=proteins, fats=fats, carbohydrates=carbohydrates,
                             description=description, owner_id=owner_id)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def get_user_products_by_id(db: Session, owner_id: int):
    return db.query(models.Product).filter(models.Product.owner_id == owner_id).all()
