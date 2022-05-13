from api import api
from os import environ

def start():
    port = int(environ.get("PORT", 8080))

    if __name__ == '__main__':
        api.run('0.0.0.0', port=port)

if __name__ == '__main__':
    start()