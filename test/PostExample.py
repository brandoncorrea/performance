import requests

from data import RandomData
from core import ThreadExecutor

random_data = RandomData()


def post_request():
    password = random_data.characters(8)
    name = random_data.name() + ' ' + random_data.name()
    data = {'name': name,
            'phone': random_data.phone_number(),
            'email': name + random_data.characters(4) + random_data.email_provider(),
            'password': password}
    x = requests.post('https://example.com/endpoint', data=data)
    print(x.status_code)


if __name__ == '__main__':
    ThreadExecutor.spin(50, post_request)
