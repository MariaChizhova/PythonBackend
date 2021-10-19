from app import requests, models
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_user():
    with SessionLocal() as db:
        requests.add_user(db=db, name="User1", password="password1", email="user1@gmail.com")
        requests.add_user(db=db, name="User2", password="password2", email="user2@gmail.com")
        requests.add_user(db=db, name="User3", password="password3", email="user3@gmail.com")
        assert requests.get_user_by_email(db=db, email="user1@gmail.com").name == "User1"
        assert requests.get_user_by_id(db=db, user_id=1).name == "User1"
        assert requests.get_user_by_email(db=db, email="user2@gmail.com").name == "User2"
        assert requests.get_user_by_id(db=db, user_id=2).name == "User2"
        assert requests.get_user_by_email(db=db, email="user3@gmail.com").name == "User3"
        assert requests.get_user_by_id(db=db, user_id=3).name == "User3"
        assert len(requests.get_users(db=db)) == 3


def test_products():
    with SessionLocal() as db:
        requests.add_user_product(db=db, name="apple", calories="82.7", proteins="0.7", fats="0.7",
                                  carbohydrates="17.2",
                                  description="Yammy", owner_id="1")
        requests.add_user_product(db=db, name="banana", calories="95", proteins="1.5", fats="0.2", carbohydrates="21.8",
                                  description="Yammy", owner_id="2")
        requests.add_user_product(db=db, name="grapes", calories="65", proteins="0.6", fats="0.2", carbohydrates="16.8",
                                  description="Yammy", owner_id="2")
        assert len(requests.get_user_products_by_id(db=db, owner_id=1)) == 1
        assert len(requests.get_user_products_by_id(db=db, owner_id=2)) == 2
        assert len(requests.get_user_products_by_id(db=db, owner_id=3)) == 0
        assert len(requests.get_products(db=db)) == 3
        assert requests.get_user_products_by_id(db=db, owner_id=1)[0].name == "apple"
        assert requests.get_user_products_by_id(db=db, owner_id=2)[0].name == "banana"
        assert requests.get_user_products_by_id(db=db, owner_id=2)[1].name == "grapes"
