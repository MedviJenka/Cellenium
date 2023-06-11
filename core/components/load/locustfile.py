from locust import HttpUser, task, between
from core.components.config.reader import ConfigReader
from dataclasses import dataclass
import requests


@dataclass
class QuickstartUser(HttpUser):

    wait_time = between(1, 5)
    config = ConfigReader()

    @task
    def hello_world(self):
        json = self.config.read('path', 'request')
        _request = requests.Request(json=json)
        self.client.get(_request)


if __name__ == "__main__":
    hello = QuickstartUser()
    hello.hello_world()
