import logging
import requests
import warnings
from typing import Optional
from dataclasses import dataclass
from core.infrastructure.modules.methods import log
from core.infrastructure.api.constants import Authorization


warnings.filterwarnings('ignore')


@dataclass
class RestRequest:

    """
    class_params: base_url ........................... A string representing the base URL for the HTTP requests.

    class_params: status_code ........................ A boolean, if True, returns response status code.

    :params: query_path (required) ................... A string representing the endpoint.
                                                       path to be appended to the base URL.
    :params: headers (optional) ...................... A dictionary containing the headers to be sent with the request.

    :params (optional) ............................... A dictionary containing the query parameters.
                                                       to be sent with the request.
    :params: verify (optional) ....................... A boolean indicating whether to verify the SSL certificate.

    :returns: response in a json format
    """

    base_url: str = 'https://qastng.ai-logix.net'
    status_code: bool = False

    def get_request(self, query_path: str, params=Optional[dict], verify=False) -> any:
        url = f'{self.base_url}/{query_path}'
        response = requests.get(url, headers=Authorization.HEADERS, params=params, verify=verify)
        if self.status_code:
            return f'response: {response.status_code}'

        log(level=logging.DEBUG, text=f'sent {response} with status code: {response.status_code}')
        return response.json()

    def post_request(self, query_path: str, body: dict[str], params=Optional[dict], verify=False) -> dict | int:
        url = f'{self.base_url}/{query_path}'
        response = requests.post(url, headers=Authorization.HEADERS, json=body, params=params, verify=verify)
        if self.status_code:
            return response.status_code

        log(level=logging.DEBUG, text=f'sent {response} with status code: {response.status_code}')
        return response.json()

    def put_request(self, query_path: str, body: dict[str], params=Optional[dict], verify=False) -> dict | int:
        url = f'{self.base_url}/{query_path}'
        response = requests.put(url, headers=Authorization.HEADERS, json=body, params=params, verify=verify)
        if self.status_code:
            return response.status_code

        log(level=logging.DEBUG, text=f'sent {response} with status code: {response.status_code}')
        return response.json()

    def delete_request(self, query_path: str, params=Optional[dict], verify=False) -> dict | int:
        url = f'{self.base_url}/{query_path}'
        response = requests.delete(url, headers=Authorization.HEADERS, params=params, verify=verify)
        if self.status_code:
            return response.status_code

        log(level=logging.DEBUG, text=f'sent {response} with status code: {response.status_code}')
        return response.json()
