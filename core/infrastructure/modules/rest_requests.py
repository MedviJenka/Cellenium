import requests
from dataclasses import dataclass, field
from requests import Response
from typing import Optional


@dataclass
class RestRequests:

    base_url: str
    query: str
    api_key: Optional[str] = None
    headers: dict = field(default_factory=dict[str])

    def generate_request(self, method: str, params: dict[str, str] = None) -> Response:
        match method:
            case "GET":
                respond = requests.get(f'{self.base_url}/{self.query}', params=params, headers=self.headers)
                return respond.json()
            case "POST":
                respond = requests.post(f'{self.base_url}/{self.query}', params=params, headers=self.headers)
                return respond.json()
            case "PUT":
                respond = requests.put(f'{self.base_url}/{self.query}', params=params, headers=self.headers)
                return respond.json()
            case "DELETE":
                respond = requests.delete(f'{self.base_url}/{self.query}', params=params, headers=self.headers)
                return respond.json()
            case _:
                raise Exception('no such method')


if __name__ == '__main__':
    request = RestRequests(base_url='http://maps.googleapis.com',
                           query='maps/api/geocode/json')
    print(request.generate_request(method="GET",
                                   params={'address': 'delhi technological university'}))
