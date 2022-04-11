class Account:

    def __init__(self, username, password, phone_number, email):
        self.email = Account.check_email(email)
        self.phone_number = Account.check_phone(phone_number)
        self.password = Account.check_password(password)
        self.username = Account.check_email(username)

    @staticmethod
    def check_username(username):
        pass

    @staticmethod
    def check_password(password):
        pass

    @staticmethod
    def check_phone(phone_number):
        pass

    @staticmethod
    def check_email(email):
        pass

