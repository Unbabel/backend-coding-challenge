import requests
import os
import redis
#from config import Config
from rq import Worker, Queue, Connection

#conn = redis.from_url(Config.REDISTOGO_URL)

listen = ['default']
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
conn = redis.from_url(redis_url)

payload = {
    'text': 'Hello world',
    'source_language': 'en',
    'target_language': 'pt',
    'text_format': 'text',
}

# r = requests.post(Config.URL, json=payload, headers=Config.HEADERS)
# print(r)

if __name__ == '__main__':
    with Connection(conn):
        #worker = Worker(list(map(Queue, Config.LISTEN)))
        worker = Worker(list(map(Queue, listen)))
        worker.work()
