import requests
import warnings
from dataclasses import dataclass
from tests.CallServiceAPI.constants import *

warnings.filterwarnings('ignore')


@dataclass
class RestRequest:

    base_url: str = 'https://nextgenkube.ai-logix.net'
    status_code: bool = False

    def get_request(self, query_path: str, headers=None, params=None, verify=False) -> dict | int:
        url = f'{self.base_url}/{query_path}'
        response = requests.get(url, headers=headers, params=params, verify=verify)
        if self.status_code:
            return response.status_code
        return response.json()

    def post_request(self, query_path: str, body: dict[str], headers=None, params=None, verify=False) -> dict | int:
        url = f'{self.base_url}/{query_path}'
        response = requests.post(url, headers=headers, json=body, params=params, verify=verify)
        if self.status_code:
            return response.status_code
        return response.json()

    def put_request(self, query_path: str, body: dict[str], headers=None, params=None, verify=False) -> dict | int:
        url = f'{self.base_url}/{query_path}'
        response = requests.put(url, headers=headers, json=body, params=params, verify=verify)
        if self.status_code:
            return response.status_code
        return response.json()

    def delete_request(self, query_path: str, headers=None, params=None, verify=False) -> dict | int:
        url = f'{self.base_url}/{query_path}'
        response = requests.delete(url, headers=headers, params=params, verify=verify)
        if self.status_code:
            return response.status_code
        return response.json()


class AdvancedFunctionality(RestRequest):

    """
    :params: index ............. iterate through jsons dictionary
    :params: _from, to ......... amount range
    """

    def get_db_id(self, index: int, query_path: str) -> str:
        result = self.get_request(query_path=query_path,
                                  headers=Authorization.HEADERS)
        return result['data'][index]['id']

    def get_multiple_db_ids(self, _from: int, to: int, query_path: str, display=False) -> list[str]:
        result = [self.get_db_id(a, query_path=query_path) for a in range(_from, to)]
        if display:
            print(result)
        else:
            return result
