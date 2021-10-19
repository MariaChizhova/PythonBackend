from collections import defaultdict
from app.models.product_model import Product
from fastapi import HTTPException


class Products:

    def __init__(self):
        self.products = defaultdict(list)

    @staticmethod
    def check_name_correctness(name: str):
        if name == "":
            raise HTTPException(status_code=400, detail="Invalid name")

    def add_item(self, product: Product):
        self.check_name_correctness(product.name)
        date = product.date.date()
        self.products[date].append(product)
        return product

    def calculate(self, item_type: str):
        result = []
        for date in self.products:
            total = 0
            for item in self.products[date]:
                if item_type == "calories":
                    total += item.calories
                elif item_type == "proteins":
                    total += item.proteins
                elif item_type == "fats":
                    total += item.fats
                elif item_type == "carbohydrates":
                    total += item.carbohydrates
            result.append({date: total})
        return result

    def mean_between_days(self, first_day, last_day, number):
        total_sum = 0
        for date in self.products:
            if first_day <= date <= last_day:
                total_sum += sum(item.calories for item in self.products[date])
        return total_sum / (number + 1)

    def total_by_date(self, date):
        return self.products[date]

    def total(self):
        return self.products

