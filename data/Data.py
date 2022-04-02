import json
import string


def characters():
    return string.ascii_letters + string.digits + '!@#$%^&*()'


def load_json(file_name):
    json.loads(open(file_name).read())


def email_providers():
    load_json('email_provider.json')


def names():
    load_json('name.json')
