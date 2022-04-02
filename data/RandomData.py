import random
import os
import Data


class RandomData:
    chars = []
    email_providers = []
    names = []

    def __init__(self):
        random.seed = os.urandom(1024)
        self.chars = Data.characters()
        self.email_providers = Data.email_providers()
        self.names = Data.names()

    def characters(self, length):
        return ''.join(random.choice(self.chars) for _ in range(length))

    def email_provider(self):
        random.choice(self.email_providers)

    def name(self):
        random.choice(self.names)

    @staticmethod
    def phone_number():
        str(random.randint(1000000000, 9999999999))


