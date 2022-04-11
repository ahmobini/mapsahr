import re, hashlib

class Account:
    test = []

    def __init__(self, username, password, phone, email):
        self.username = input('enter username: ')
        self.password = check_password(password)
        self.phone = check_phone(phone)
        self.email = input('enter email: ')

    @staticmethod
    def check_username(username):
        if not re.search("^\w+_\w+$",username):
            raise Exception('invalid username')
        return username

    @classmethod
    def check_password(cls, password):
        if not all([re.search("[a-z]|[A-Z]+[0-9]\d{1}$", password), len(password) >= 8]):
            raise Exception('invalid password')
        encoded = password.encode('utf-8')
        return hashlib.sha256(encoded)

    @classmethod
    def check_phone(cls, phone):
        if not (re.search("^((\+989)|(09))+[0-3,9]\d{8}$", phone)):
            raise Exception('invalid phone number')
        return phone

    @staticmethod
    def check_email(email):
        if not re.search("([A-Za-z0-9]+[.-_])+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,5})+",email):
            raise Exception('invalid email')
        return email


if __name__ == '__main__':
    user = Account('amir_hussein_mobini', 'CH.ristiano07', '+989124756047', 'amir.hussein.mobini@gmail.com')


