import requests
import warnings
from dataclasses import dataclass


warnings.filterwarnings('ignore')
token = ""
_headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": token,
    "tenantId": ""
}


@dataclass
class RestRequest:

    base_url: str = 'https://nextgenkube.ai-logix.net'

    def get_request(self, query_path: str, headers=None, params=None, verify=False) -> dict:
        url = f'{self.base_url}/{query_path}'
        response = requests.get(url, headers=headers, params=params, verify=verify)
        return response.json()

    def post_request(self, query_path: str, body, headers=None, params=None, verify=True) -> dict:
        url = f'{self.base_url}/{query_path}'
        response = requests.post(url, headers=headers, json=body, params=params, verify=verify)
        return response.json()

    def put_request(self, query_path: str, body, headers=None, params=None, verify=True) -> dict:
        url = f'{self.base_url}/{query_path}'
        response = requests.put(url, headers=headers, json=body, params=params, verify=verify)
        return response.json()

    def delete_request(self, query_path: str, body, headers=None, params=None, verify=True) -> dict:
        url = f'{self.base_url}/{query_path}'
        response = requests.delete(url, headers=headers, json=body, params=params, verify=verify)
        return response.json()


class CallServiceFunctionality(RestRequest):
    def get_db_id(self, index: int) -> str:
        result = self.get_request(query_path='api/calls?sortBy=startTime&order=desc&pageNumber=1&pageSize=100',
                                  headers=_headers)
        return result['data'][index]['id']
