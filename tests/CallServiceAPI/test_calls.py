from tests.CallServiceAPI.api_module import AdvancedFunctionality
from tests.CallServiceAPI.constants import CallTypes, Users, Authorization, MediaTypes


advanced = AdvancedFunctionality()
db_id = advanced.get_db_id(index=1, query_path='api/calls?sortBy=startTime&order=desc&pageNumber=1&pageSize=100')


def test_start_call() -> None:

    _body = {
        "participants": [
            {
                "joinTime": "2023-03-15T08:39:37.231Z",
                "leaveTime": "2023-03-15T08:39:37.231Z",
                "upn": Users.USER1_NAME,
                "displayName": Users.USER1_NAME,
                "oid": Users.USER1_OID,
                "id": db_id
            },
            {
                "joinTime": "2023-03-15T08:39:37.231Z",
                "leaveTime": "2023-03-15T08:39:37.231Z",
                "upn": Users.USER2_NAME,
                "displayName": Users.USER2_NAME,
                "oid": Users.USER2_OID,
                "id": db_id
            },
        ],
        "startTime": "2023-03-15T08:39:37.231Z",
        "target": {
            "userGlobalId": Users.USER2_OID,
            "upn": Users.USER2_NAME,
            "displayName": Users.USER2_NAME,
            "azureOid": Users.USER2_OID
        },
        "callDirection": "incoming",
        "callType": CallTypes.INTERNAL_P2P,
        "azureTenantId": Authorization.TENANT_ID,
        "called": {
            "upn": Users.USER1_NAME,
            "displayName": Users.USER1_NAME,
            "oid": Users.USER1_OID,
            "id": db_id
        },
        "calling": {
            "upn": Users.USER2_NAME,
            "displayName": Users.USER2_NAME,
            "oid": Users.USER2_OID,
            "id": db_id
        },
        "sysCallId": "string",
        "sipCallId": "string",
        "conferenceUrl": "string",
        "transferedBy": {
            "upn": "user@example.com",
            "displayName": "string",
            "oid": "string",
            "id": "string"
        },
        "transferTo": {
            "upn": "user@example.com",
            "displayName": "string",
            "oid": "string",
            "id": "string"
        },
        "onBehalfOf": {
            "upn": "user@example.com",
            "displayName": "string",
            "oid": "string",
            "id": "string"
        },
        "retentionId": "string",
        "recordingGroups": [
            "string"
        ]
    }

    print(advanced.post_request(query_path='api/calls', headers=Authorization.HEADERS, body=_body))
    print(db_id)


def test_answer_call() -> None:
    _body = {
        "answeringParty": {
            "upn": Users.USER2_NAME,
            "displayName": Users.USER2_NAME,
            "oid": Users.USER2_OID,
            "id": db_id
        },
        "answerTime": "2023-03-15T09:06:46.948Z"
    }
    result = advanced.put_request(query_path=f'api/calls/{db_id}/answerCall', headers=Authorization.HEADERS, body=_body)
    assert result == {'statusCode': 'ok', 'description': ''}


def test_end_call() -> None:
    advanced = AdvancedFunctionality(status_code=True)
    _body = {
        "releaseCause": "normal",
        "releaseTime": "2023-03-15T16:46:56.045Z",
        "content": {
            "mediaType": MediaTypes.AUDIO,
            "path": "string",
            "audioContent": {
              "subPath": "string",
              "fileName": "string",
              "status": "pending"
            }
        }
    }
    result = advanced.put_request(query_path=f'api/calls/{db_id}/endCall', headers=Authorization.HEADERS, body=_body)
    assert result == 200
