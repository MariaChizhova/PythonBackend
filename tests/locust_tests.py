from locust import HttpUser, task


class Testing(HttpUser):
    @task(1)
    def test_create_item(self):
        new_product = {
            "name": "apple",
            "calories": 100,
            "proteins": 20,
            "fats": 30,
            "carbohydrates": 40,
            "date": "2021-09-26T10:33:48.257Z",
            "description": "string"
        }
        self.client.post("/products/", json=new_product)

    @task(2)
    def test_get_calories(self):
        self.client.get("/calculate/proteins/")

    @task(3)
    def test_get_mean(self):
        self.client.get("/calculate_mean/10")
