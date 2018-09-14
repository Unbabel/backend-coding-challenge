from config import Config
import requests

payload = {
    'text': 'Hello world',
    'source_language': 'en',
    'target_language': 'pt',
    'text_format': 'text',
}
# r = requests.post(Config.URL, json=payload, headers=Config.HEADERS)
# print(r)