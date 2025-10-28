from typing import List

class Bank:

    def __init__(self, balance: List[int]):
        self.n = len(balance)
        self.balances = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 1 <= account1 <= self.n and 1 <= account2 <= self.n and money <= self.balances[account1 - 1]:
            self.balances[account1 - 1] -= money
            self.balances[account2 - 1] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if 1 <= account <= self.n:
            self.balances[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if 1 <= account <= self.n and money <= self.balances[account - 1]:
            self.balances[account - 1] -= money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
