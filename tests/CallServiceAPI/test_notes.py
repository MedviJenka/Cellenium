from tests.CallServiceAPI.api_module import AdvancedFunctionality
from tests.CallServiceAPI.constants import Authorization


call = AdvancedFunctionality()
api_query = 'api/calls?sortBy=startTime&order=desc&pageNumber=1&pageSize=100'
db_id = call.get_db_id(index=1, query_path=api_query)


def test_create_note() -> dict[str]:

    _body = {
        "content": "test string",
        "createdAt": "2023-03-13T13:40:45.388Z"
    }

    result = call.post_request(query_path=f'api/calls/{db_id}/notes', headers=Authorization.HEADERS, body=_body)
    assert result['visibility'] == 'public'
    assert result['content'] == 'test string'

    return {
        "db_id": result['id'],
        "note_id": result['createdBy']['id']
    }


def test_edit_note() -> None:
    _body = {
        "content": "edited note"
    }
    advanced = AdvancedFunctionality()
    note_id = test_create_note()['note_id']
    result = advanced.put_request(query_path=f'api/calls/{db_id}/notes/{note_id}',
                                  headers=Authorization.HEADERS,
                                  body=_body)
    print(result)
    assert result == {"statusCode": "continue", "description": "edited note"}


def test_note_state_is_public() -> None:
    _body = {
        "content": "test string",
        "createdAt": "2023-03-13T13:40:45.388Z"
    }
    result = call.post_request(query_path=f'api/calls/{db_id}/notes', headers=Authorization.HEADERS, body=_body)
    print(result)
    assert result['visibility'] == 'public'


def test_note_content() -> None:
    _body = {
        "content": "test string",
        "createdAt": "2023-03-13T13:40:45.388Z"
    }
    result = call.post_request(query_path=f'api/calls/{db_id}/notes', headers=Authorization.HEADERS, body=_body)
    print(result)
    assert result['content'] == 'test string'


def test_create_and_delete_note() -> None:

    _body = {
        "content": "test string",
        "createdAt": "2023-03-13T13:40:45.388Z"
    }

    advanced = AdvancedFunctionality()
    result = advanced.post_request(query_path=f'api/calls/{db_id}/notes', headers=Authorization.HEADERS, body=_body)
    note_id = result['createdBy']['id']
    print(note_id)
    delete_result = advanced.delete_request(query_path=f'api/calls/{db_id}/notes/{note_id}',
                                            headers=Authorization.HEADERS)

    assert delete_result == {
        "statusCode": "ok",
        "description": ""
    }
