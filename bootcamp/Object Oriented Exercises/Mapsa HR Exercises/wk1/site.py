import hashlib
from typing import Dict, List
from account import Account
from factor import Factor
from product import Product


class Site:
    def __init__(self, url: str):
        self.url = url
        self.registered_users: List[Account] = []
        self.active_users: List[Account] = []
        self.inventory: Dict[Product, int] = {}
        self.purchases: List[Factor] = []

    def register(self, new_account: Account) -> str:
        filter_accounts = [account for account in self.registered_users if account.username == new_account.username]
        if len(filter_accounts) > 0:
            raise Exception('user already registered.')
        self.registered_users.append(new_account)
        return 'register successful.'

    def login(self, username = None, email = None, password = None) -> str:
        filter_accounts = []
        password = hashlib.sha256(password.encode('utf-8'))
        if username and email and password:
            filter_accounts = [a for a in self.registered_users if a.username == username and a.email == email and a.password.digest() == password.digest()]
        elif username and password:
            filter_accounts = [a for a in self.registered_users if a.username == username and a.password.digest() == password.digest()]
        elif email and password:
            filter_accounts = [a for a in self.registered_users if a.email == email and a.password.digest() == password.digest()]
        if len(filter_accounts) > 0:
            account = filter_accounts[0]
            if self.is_authenticated(account=account):
                return "user already logged in"
            self.active_users.append(account)
            return "login successful"
        else:
            return "invalid login"


    def logout(self, account: Account) -> str:
        filtered_accounts = [a for a in self.active_users if a.username == account.username]
        if len(filtered_accounts) == 0:
            return "user is not logged in"
        self.active_users = [a for a in self.active_users if a.username != account.username]
        return "logout successful"

    def is_authenticated(self, account: Account) -> bool:
        return len([a for a in self.active_users if a.username == account.username]) > 0

    def purchase(self, account: Account, product: Product, count: int):
        if not self.is_authenticated(account):
            return "user is not logged in"
        matched_products = \
            [(prod, prod_count) for prod, prod_count in self.inventory.items() if prod.id == product.id]
        if len(matched_products) == 0:
            return "no such product in this site"
        if matched_products[0][1] < count:
            return f"requested {count} {product.name} is larger than available products (= {matched_products[0][1]}) in stock."
        factor = Factor(account, product, count)
        self.purchases.append(factor)
        self.inventory[matched_products[0][0]] -= count
        return "purchase successful"

if __name__ == '__main__':
    site = Site('shalghamkala.com')
    user = Account(
        username = 'alireza_helali', phone = '09163311945', email = 'a.helali1995@gmail.com', password = "ALIgholi123!"
    )

    register_result = site.register(user)
    print(register_result)

    login_result = site.login(username='alireza_helali', password='ALIgholi123!')
    print(login_result)
    print(site.active_users)
 
    # logout_result = site.logout(user)
    # print(logout_result)
    # print(site.active_users)
    
    # purchase start here

    p1 = Product("1", "Harry Poter")
    p2 = Product("2", "Game of Thrones")
    # better to have a method for admin of site to update inventory
    site.inventory = {
        p1: 5,
        p2: 3
    }

    purchase_result = site.purchase(user, p1, 2)
    print(purchase_result)

    purchase_result = site.purchase(user, p1, 2)
    print(purchase_result)

    purchase_result = site.purchase(user, p1, 2)
    print(purchase_result)
    

    d = {
        "salam": 1,
        "majid": 2,
    }