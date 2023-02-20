import requests
from dataclasses import dataclass


global_url = 'https://nextgenkube.ai-logix.net'
global_headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "",
    "tenantId": "ad41d6c3-67f0-47cc-9de3-e07fd185c1c7"
}


@dataclass
class RestRequest:

    base_url: str = global_url

    def get_request(self, path: str, headers=None, params=None, verify=True):
        url = f'{self.base_url}/{path}'
        response = requests.get(url, headers=headers, params=params, verify=verify)
        return response

    def post_request(self, path: str, body, headers=None, params=None):
        url = self.base_url + path
        response = requests.post(url, headers=headers, json=body, params=params)
        return response.json()

    def put_request(self, path: str, body, headers=None, params=None):
        url = self.base_url + path
        response = requests.put(url, headers=headers, json=body, params=params)
        return response.json()

    def delete_request(self, path: str, body, headers=None, params=None):
        url = self.base_url + path
        response = requests.delete(url, headers=headers, json=body, params=params)
        return response.json()


def test_call() -> None:
    rest = RestRequest()
    result = rest.get_request(path='api/calls', headers=global_headers, verify=False)
    assert result == 401
