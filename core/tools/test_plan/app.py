import pyChatGPT
from core.infrastructure.modules.reader import read_json


TOKEN = read_json(path=r'C:\Users\evgenyp\Cellenium\core\tools\test_plan\token.json', value='token')


def ai_test_plan(text: str) -> None:
    session_api = pyChatGPT.ChatGPT(session_token=TOKEN)
    response = session_api.send_message(text)
    result = "".join(response.get(f'write a test plan for {text}'))
    print(result)


ai_test_plan("write a 3 step test plan for snake game")
