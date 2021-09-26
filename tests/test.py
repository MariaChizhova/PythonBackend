import pytest
from app.product_model import Product
from app.calculations import Products
import datetime


def test_check_name_correctness():
    products = Products()
    products.check_name_correctness("Masha")


@pytest.mark.xfail()
def test_check_name_correctness_fail():
    products = Products()
    products.check_name_correctness("")


def test_create_item():
    products = Products()
    date = datetime.datetime(2021, 9, 25)
    products.add_item(
        Product(name="apple", calories=47, proteins=0.4, fats=0.4, carbohydrates=9.8, date=date))
    assert len(products.products) == 1
    assert len(products.products[date.date()]) == 1
    assert products.products[date.date()] == [
        Product(name="apple", calories=47, proteins=0.4, fats=0.4, carbohydrates=9.8, date=date, desctiption=None)]


def add_products():
    products = Products()
    date = datetime.datetime(2021, 9, 23)
    products.add_item(
        Product(name="potato", calories=86, proteins=1.7, fats=0.1, carbohydrates=18.2, date=date))
    products.add_item(
        Product(name="tomato", calories=18, proteins=0.9, fats=0.2, carbohydrates=2.7, date=date))
    products.add_item(
        Product(name="cucumber", calories=16, proteins=0.7, fats=0.1, carbohydrates=3.1, date=date))

    date = datetime.datetime(2021, 9, 24)
    products.add_item(
        Product(name="bread", calories=266, proteins=8.9, fats=3.3, carbohydrates=46.7, date=date))
    products.add_item(
        Product(name="cherry", calories=52, proteins=0.8, fats=0.2, carbohydrates=10.6, date=date))
    products.add_item(
        Product(name="raspberries", calories=52, proteins=1.2, fats=0.7, carbohydrates=5.4, date=date))

    date = datetime.datetime(2021, 9, 25)
    products.add_item(
        Product(name="apple", calories=47, proteins=0.4, fats=0.4, carbohydrates=9.8, date=date))
    products.add_item(
        Product(name="banana", calories=95, proteins=1.5, fats=0.2, carbohydrates=21.8, date=date))
    products.add_item(
        Product(name="orange", calories=43, proteins=0.9, fats=0.2, carbohydrates=8.1, date=date))
    return products


def test_calculate_calories():
    products = add_products()
    assert products.calculate("calories") == [{datetime.date(2021, 9, 23): 120},
                                              {datetime.date(2021, 9, 24): 370},
                                              {datetime.date(2021, 9, 25): 185}]


def test_calculate_proteins():
    products = add_products()
    assert products.calculate("proteins") == [{datetime.date(2021, 9, 23): 3.3},
                                              {datetime.date(2021, 9, 24): 10.9},
                                              {datetime.date(2021, 9, 25): 2.8}]


def test_calculate_fats():
    products = add_products()
    assert products.calculate("fats") == [{datetime.date(2021, 9, 23): 0.4},
                                          {datetime.date(2021, 9, 24): 4.2},
                                          {datetime.date(2021, 9, 25): 0.8}]


def test_calculate_carbohydrates():
    products = add_products()
    assert products.calculate("carbohydrates") == [{datetime.date(2021, 9, 23): 24},
                                                   {datetime.date(2021, 9, 24): 62.7},
                                                   {datetime.date(2021, 9, 25): 39.7}]


def test_calculate_mean():
    products = add_products()
    last_day = datetime.date(2021, 9, 25)
    first_day = last_day - datetime.timedelta(days=2)
    second_day = last_day - datetime.timedelta(days=1)
    assert products.mean_between_days(first_day, first_day, 0) == 120.0
    assert products.mean_between_days(second_day, second_day, 0) == 370.0
    assert products.mean_between_days(last_day, last_day, 0) == 185.0
    assert products.mean_between_days(second_day, last_day, 1) == 277.5
    assert products.mean_between_days(first_day, second_day, 1) == 245
    assert products.mean_between_days(first_day, last_day, 2) == 225
    assert products.mean_between_days(last_day, last_day, 9) == 18.5


def test_total_by_date():
    products = add_products()
    date = datetime.datetime(2021, 9, 23)
    assert products.total_by_date(date.date()) == [
        Product(name="potato", calories=86, proteins=1.7, fats=0.1, carbohydrates=18.2, date=date),
        Product(name="tomato", calories=18, proteins=0.9, fats=0.2, carbohydrates=2.7, date=date),
        Product(name="cucumber", calories=16, proteins=0.7, fats=0.1, carbohydrates=3.1, date=date)]
    date = datetime.datetime(2021, 9, 24)
    assert products.total_by_date(date.date()) == [
        Product(name="bread", calories=266, proteins=8.9, fats=3.3, carbohydrates=46.7, date=date),
        Product(name="cherry", calories=52, proteins=0.8, fats=0.2, carbohydrates=10.6, date=date),
        Product(name="raspberries", calories=52, proteins=1.2, fats=0.7, carbohydrates=5.4, date=date)]
    date = datetime.datetime(2021, 9, 25)
    assert products.total_by_date(date.date()) == [
        Product(name="apple", calories=47, proteins=0.4, fats=0.4, carbohydrates=9.8, date=date),
        Product(name="banana", calories=95, proteins=1.5, fats=0.2, carbohydrates=21.8, date=date),
        Product(name="orange", calories=43, proteins=0.9, fats=0.2, carbohydrates=8.1, date=date)]
