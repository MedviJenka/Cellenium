from time import sleep
import subprocess
from tests.contract.global_variables import *


provider = 'User Service'
PATH = r'C:\Cellenium\tests\contract'


def _azure_groups(action: str) -> None:
    if action == 'create':
        subprocess.run(['powershell.exe',
                        '-File',
                        fr'{PATH}\CreateGroup.ps1'])
        sleep(60)

    elif action == 'delete':
        subprocess.run(['powershell.exe',
                        '-File',
                        fr'{PATH}\DeleteGroup.ps1'])
        sleep(60)


if __name__ == '__main__':
    _azure_groups(action='create')

# def test_get_azure_member_count() -> None:
#
#     expected = 90
#
#     (contract
#      .given('Groups Contract 1')
#      .upon_receiving('get request single item')
#      .with_request(method='get',
#                    path='/api/sync/groups/azureGroupMembersCount/845e4dd8-78aa-49cd-bd44-fbeb622ce809/false',
#                    headers=headers)
#      .will_respond_with(200, body=pact.like(expected)))
#
#     with contract:
#         result = client.get_request(
#             path='/api/sync/groups/azureGroupMembersCount/845e4dd8-78aa-49cd-bd44-fbeb622ce809/false',
#             headers=headers)
#
#     assert result == expected
#
#
# def test_get_groups() -> None:
#
#     expected = {
#         "dbId": "",
#         "displayName": "",
#         "azId": "",
#         "removedFromAzure": False,
#         "usersCount": 0
#     }
#
#     (contract
#      .given('Groups Contract 2')
#      .upon_receiving('get request single item')
#      .with_request(method='get', path='/api/sync/groups/', headers=headers)
#      .will_respond_with(200, body=pact.eachlike(expected)))
#
#     with contract:
#         result = client.get_request(path='/api/sync/groups/',
#                                     headers=headers)
#
#     assert result == [expected]
#
#
# def test_get_azure_group_by_name() -> None:
#     expected = {
#         "displayName": "ST",
#         "azId": "104b2b0c-d1a7-46b2-a6ca-958b17b6b133"
#     }
#
#     (contract
#      .given('Groups Contract 3')
#      .upon_receiving('get request list of items')
#      .with_request(method='get', path='/api/sync/groups/azureGroupsByName/st/5', headers=headers)
#      .will_respond_with(200, body=pact.eachlike(expected)))
#
#     with contract:
#         result = client.get_request(path='/api/sync/groups/azureGroupsByName/st/5',
#                                     headers=headers)
#
#     assert result == [expected]
#
#
# def test_get_recording_groups() -> None:
#
#     expected = {
#         "dbId": "",
#         "displayName": "",
#         "azId": "",
#         "removedFromAzure": False,
#         "usersCount": 0
#     }
#
#     (contract
#      .given('Groups Contract 4')
#      .upon_receiving('get request single item')
#      .with_request(method='get', path='/api/sync/groups/recordingGroups/', headers=headers)
#      .will_respond_with(200, body=pact.eachlike(expected)))
#
#     with contract:
#         result = client.get_request(path='/api/sync/groups/recordingGroups/',
#                                     headers=headers)
#
#     assert result == [expected]
#
#
# def test_add_group_member() -> None:
#
#     # _azure_groups(action='create')
#
#     body = {
#         "displayName": "@STNGGroup1",
#         "azId": "0eaecb5d-32e3-400a-be13-94b77d7ca65e",
#         "transitive": True
#     }
#
#     expected = {
#         "dbId": "63d679614c248aad5bba4565",
#         "displayName": "st-subgroup1-test-ooo",
#         "azId": "14a05d00-7b09-4121-a9f4-b4d2f26b79b3",
#         "removedFromAzure": False,
#         "usersCount": 4
#     }
#
#     (contract
#      .given('Groups Contract 5')
#      .upon_receiving('post request single item')
#      .with_request(method='post', path='/api/sync/groups/', headers=headers)
#      .will_respond_with(200, body=pact.eachlike(expected)))
#
#     with contract:
#         result = client.post_request(path='/api/sync/groups/',
#                                      body=body,
#                                      headers=headers)
#
#     assert result == [expected]
#
#     # _azure_groups(action='delete')
#
#
# def test_verify_contract() -> None:
#     result = pact.verify_pact(base_url)
#     assert result == 0
