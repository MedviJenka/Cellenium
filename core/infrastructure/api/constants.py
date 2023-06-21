class Authorization:

    """
    :TODO: check in wireshark both postman and python requests and see the differences

    """

    TENANT_ID = ""
    TOKEN = ""
    HEADERS = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": TOKEN
    }
