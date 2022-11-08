from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")


if __name__ == "__main__":
    hello = HelloWorldUser()
    hello.hello_world()
