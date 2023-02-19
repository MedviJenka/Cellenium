import os


CREDENTIALS = {
    "display_name": "jenia-01-aad-app",
    "app_id": "c4cfb335-c19b-4959-9689-dd0be68c1962",
    "object_id": "d5eb4edc-1b91-43be-ae21-24d8cad0cb25",
    "tenant_id": "ad41d6c3-67f0-47cc-9de3-e07fd185c1c7"
}


if __name__ == '__main__':
    print(CREDENTIALS["display_name"])
    os.system(f'pylint {__file__}')
