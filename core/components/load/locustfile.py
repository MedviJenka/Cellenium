import time
from locust import HttpUser, task, between


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("https://www.google.com")


class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello_world(self):
        self.client.get("https://www.google.com")

    @task(3)
    def view_items(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")
            time.sleep(1)

    def on_start(self):
        self.client.post("/login", json={"username":"foo", "password":"bar"})


if __name__ == "__main__":
    hello = HelloWorldUser()
    hello.hello_world()
