import requests

from core import threadexecutor


def request():
    print(requests.get('https://example.com/endpoint').status_code)


if __name__ == '__main__':
    threadexecutor.spin(50, request)
