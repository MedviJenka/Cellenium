import openai


API_KEY = "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"
openai.api_key = API_KEY
prompt = 'test'
response = openai.Completion.create(engine='text-davinci-002', prompt=prompt, max_tokens=1)
print(response)
