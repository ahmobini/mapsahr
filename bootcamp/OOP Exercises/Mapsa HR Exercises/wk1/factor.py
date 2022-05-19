from account import Account
from product import Product


class Factor:
    def __init__(self, account: Account, product: Product, count: int):
        self.account = account
        self.product = product
        self.count = count
