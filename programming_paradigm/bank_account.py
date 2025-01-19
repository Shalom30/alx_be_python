class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return self.account_balance
        else:
            print("Sorry! insufficient funds!!")

    def display_balance(self):
        print(f"Current balance $[{self.account_balance}]")
