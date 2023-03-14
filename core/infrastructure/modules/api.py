import requests
import warnings
from dataclasses import dataclass

warnings.filterwarnings('ignore')

TOKEN = ""

HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": TOKEN,
    "tenantId": "ad41d6c3-67f0-47cc-9de3-e07fd185c1c7"
}


@dataclass
class RestRequest:

    base_url: str = 'https://nextgenkube.ai-logix.net'

    def get_request(self, query_path: str, headers=None, params=None, verify=False) -> dict:
        url = f'{self.base_url}/{query_path}'
        response = requests.get(url, headers=headers, params=params, verify=verify)
        return response.json()

    def post_request(self, query_path: str, body, headers=None, params=None, verify=False) -> dict:
        url = f'{self.base_url}/{query_path}'
        response = requests.post(url, headers=headers, json=body, params=params, verify=verify)
        return response.json()

    def put_request(self, query_path: str, body, headers=None, params=None, verify=False) -> dict:
        url = f'{self.base_url}/{query_path}'
        response = requests.put(url, headers=headers, json=body, params=params, verify=verify)
        return response.json()

    def delete_request(self, query_path: str, body, headers=None, params=None, verify=False) -> dict:
        url = f'{self.base_url}/{query_path}'
        response = requests.delete(url, headers=headers, json=body, params=params, verify=verify)
        return response.json()


class AdvancedFunctionality(RestRequest):

    """
    :params: index ............. iterate through jsons dictionary
    """

    def get_db_id(self, index: int) -> str:
        result = self.get_request(query_path='api/calls?sortBy=startTime&order=desc&pageNumber=1&pageSize=100',
                                  headers=HEADERS)
        return result['data'][index]['id']

    def get_multiple_db_ids(self, _from: int, to: int, display=False) -> list[str]:
        result = [self.get_db_id(a) for a in range(_from, to)]
        if display:
            print(result)
        else:
            return result


def test_note_visibility() -> None:
    _body = {
        "content": "test string",
        "createdAt": "2023-03-13T13:40:45.388Z"
    }
    call = AdvancedFunctionality()
    db_id = call.get_db_id(index=1)
    result = call.post_request(query_path=f'api/calls/{db_id}/notes', headers=HEADERS, body=_body)
    assert result['visibility'] == 'public'


def test_get_all_calls() -> None:
    request = RestRequest()
    request.get_request(query_path='api/calls', headers=HEADERS)


def test_db_ids() -> None:
    advanced = AdvancedFunctionality()
    print(advanced.get_multiple_db_ids(_from=1, to=5))
