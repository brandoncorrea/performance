import json
import string


def characters():
    return string.ascii_letters + string.digits + '!@#$%^&*()'


def load_json(file_name):
    return json.loads(open(file_name).read())


def email_providers():
    return load_json('email_provider.json')


def names():
    return load_json('name.json')
