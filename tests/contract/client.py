import requests


class ServiceClient:
    """
    This class is used to simulate client requests to server
    """
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_request(self, path: str, headers=None, params=None):
        url = self.base_url + path
        response = requests.get(url, headers=headers, params=params)
        return response.json()

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
