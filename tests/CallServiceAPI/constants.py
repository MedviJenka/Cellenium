class Authorization:

    TENANT_ID = "ad41d6c3-67f0-47cc-9de3-e07fd185c1c7"

    token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuY" \
            "W1lIjoidXNlcjFAdGVuYW50MS5jb20iLCJ0aWQiOiJhZDQxZDZj" \
            "My02N2YwLTQ3Y2MtOWRlMy1lMDdmZDE4NWMxYzciLCJuYmYiOjE2" \
            "NzA4ODAwNTQsImV4cCI6MTc1NzI4MDA1MCwiaWF0IjoxNjcwODgw" \
            "MDU0LCJ1c2VySWQiOiI2M2NlNTVjN2E1MTc2NzdiMWQyNWIxMWIi" \
            "LCJTdFVzZXJJZCI6IjYzY2U1NWM3YTUxNzY3N2IxZDI1YjExYiIs" \
            "IlN0RGlzcGxheU5hbWUiOiJVc2VyMSBkaXNwbGF5IiwiaXNzIjo" \
            "iQ2FsbHNTcnYifQ.h3tKM9t1uDRVbn3zoMSN5adbzYqWjP7zVs5u21r3OnM"

    HEADERS = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": token,
        "tenantId": TENANT_ID
    }


class MediaTypes:
    AUDIO = "audio"
    VIDEO = "video"


class CallTypes:
    INTERNAL_P2P = "internal_p2p"
    FEDERATED_P2P = "federated_p2p"
    PSTN_P2P = "pstN_p2p"
    CONF_INTERNAL = "conference_Internal"
    CONF_INTERNAL_WITH_EXT_PARTICIPANTS = "conference_Internal_with_ext_participants"
    CONF_INTERNAL_WITH_PSTN_PARTICIPANTS = "conference_Internal_with_Pstn_participants"
    CONF_EXTERNAL = "conference_External"
    QUEUE = "queue"


class Users:
    USER1_OID = '3f23a10a-c4c1-4d9c-bce8-7e4966f8bec6'
    USER2_OID = 'e19a6d36-fee2-419f-a2b5-d6393db52f2d'
    USER1_NAME = 'st-teams101@smarttap.onmicrosoft.com'
    USER2_NAME = 'st-teams102@smarttap.onmicrosoft.com'


