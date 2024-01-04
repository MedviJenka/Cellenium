import boto3
from core.infrastructure.constants.data import IAM_SECRETS_CSV
from core.infrastructure.modules.get_auth_from_excel import get_access_key, get_secret_key


access_key_id = get_access_key(IAM_SECRETS_CSV)
secret_access_key = get_secret_key(IAM_SECRETS_CSV)

session = boto3.Session(aws_access_key_id=access_key_id,
                        aws_secret_access_key=secret_access_key)

s3_client = session.client('s3')
response = s3_client.list_buckets()

for bucket in response['Buckets']:
    print(bucket['Name'])
