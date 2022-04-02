import requests

from core import ThreadExecutor


def request():
    print(requests.get('https://example.com/endpoint').status_code)


if __name__ == '__main__':
    ThreadExecutor.spin(50, request)
