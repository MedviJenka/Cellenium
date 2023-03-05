from locust import HttpUser, task, between
from dataclasses import dataclass
import requests
from core.infrastructure.modules.methods import read_config


@dataclass
class QuickstartUser(HttpUser):

    wait_time = between(1, 5)

    @task
    def hello_world(self):
        json = read_config('path', 'request')
        _request = requests.Request(json=json)
        self.client.get(_request)


if __name__ == "__main__":
    hello = QuickstartUser()
    hello.hello_world()
