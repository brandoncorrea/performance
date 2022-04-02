import random
import os
import jsondata


class RandomData:
    chars = []
    email_providers = []
    names = []

    def __init__(self):
        random.seed = os.urandom(1024)
        self.chars = jsondata.characters()
        self.email_providers = jsondata.email_providers()
        self.names = jsondata.names()

    def characters(self, length):
        return ''.join(random.choice(self.chars) for _ in range(length))

    def email_provider(self):
        return random.choice(self.email_providers)

    def name(self):
        return random.choice(self.names)

    @staticmethod
    def phone_number():
        return str(random.randint(1000000000, 9999999999))


