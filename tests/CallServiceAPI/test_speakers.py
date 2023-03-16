from tests.CallServiceAPI.api_module import AdvancedFunctionality, RestRequest
from tests.CallServiceAPI.constants import Authorization


advanced = AdvancedFunctionality()


def test_dominant_speaker() -> None:
    _body = {
        "startTime": "2023-03-14T16:25:28.356Z",
        "endTime": "2023-03-14T16:25:28.356Z",
        "tenantId": "string",
        "speaker": {
            "upn": "user@example.com",
            "displayName": "string",
            "oid": "string",
            "id": "string"
        }
    }
    db_id = advanced.get_db_id(index=0, query_path='api/calls')
    result = advanced.post_request(query_path=f'api/calls/{db_id}/speakers',
                                   headers=Authorization.HEADERS,
                                   body=_body)
    assert result == {
        "statusCode": "continue",
        "description": "string"
    }


def test_get_speakers() -> None:
    rest = RestRequest(status_code=True)
    db_id = advanced.get_db_id(index=0, query_path='api/calls')
    result = rest.get_request(query_path=f'api/calls/{db_id}/speakers',
                              headers=Authorization.HEADERS)
    assert result == 200
