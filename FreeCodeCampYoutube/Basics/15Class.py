class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print(f'Current balance: {self.balance}\n Sorry, minimum balance must be maintained.')
        else:
            return BankAccount.withdraw(self, amount)


account = MinimumBalanceAccount(10)
print(account.balance)
print(account.minimum_balance)
account.deposit(20)
print(account.balance)
account.withdraw(5)
print(account.balance)
account.withdraw(7)
