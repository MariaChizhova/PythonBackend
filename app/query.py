from graphene import List, ObjectType, String, Float, Field
import json


class Product(ObjectType):
    name = String(required=True)
    calories = Float(required=True)
    description = String()


class Person(ObjectType):
    id = String(required=True)
    name = String(required=True)
    product = Field(Product)


class Query(ObjectType):
    people_list = None
    get_person = List(Person)

    async def resolve_get_person(self, info):
        with open("app/people.json") as people:
            people_list = json.load(people)
        return people_list
