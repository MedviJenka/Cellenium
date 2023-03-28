import json


with open(r"C:\Users\evgenyp\Desktop\config.json", 'r') as file:
    data = json.load(file)
    result = data['devices'][0]['extension']


def get_credentials() -> dict[str]:

    list1 = []
    list2 = []

    for each in result:
        username = each["adminUsername"]
        list1.append(username)
        password = each["adminPassword"]
        list2.append(password)

    return {
        "usernames": list1,
        "passwords": list2
    }


for each_username in get_credentials()['usernames']:
    print(each_username)

for each_password in get_credentials()['passwords']:
    print(each_password)
