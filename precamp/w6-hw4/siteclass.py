from accountclass import Account


class Site:

    def __init__(self, url):
        self.register_user = []
        self.active_user = []
        self.url = url

    def register(self, user):
        if user in self.register_user:
            raise Exception('user already registered.')
        self.register_user.append(user)
        print('register successful')

    def logout(self, user):
        if user in self.active_user:
            self.active_user.remove(user)
            return 'user logged out'
        raise Exception('user not logged in')

if __name__ == '__main__':
    useralireza = Account('alireza.helali','passwordazation', '0912345678', 'email@some@.com')