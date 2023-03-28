import json


with open(r"C:\Users\evgenyp\Desktop\config.json", 'r') as file:
    data = json.load(file)
    result = data['devices'][0]['extension']


def get_credentials() -> dict[str]:
    username = []
    password = []
    for values in data:
        for _, each in values.items():
            username.append(each['adminUsername'])
            password.append(each['adminPassword'])
    return {
        "username": username,
        "password": password
    }


print(get_credentials())
