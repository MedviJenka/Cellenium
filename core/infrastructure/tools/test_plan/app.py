import openai
from core.infrastructure.modules.reader import read_json
from core.infrastructure.constants.data import PROJECT_PATH


api_key = read_json(fr'{PROJECT_PATH}\core\infrastructure\tools\test_plan\api_key.json')
openai.organization = "org-mgjE1KXrBUojTzOG3VB1aQZT"
openai.api_key = api_key['api_key']
print(openai.Model.list())
