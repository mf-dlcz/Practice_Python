#               Defining bank account classes:

class BankAccount:
    number_of_accounts = 0

    def __init__(self, balance):
        account_number = BankAccount.number_of_accounts + 1
        self.account_number = str(account_number)
        BankAccount.number_of_accounts += 1
        self.balance = balance
    
    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def withdraw(self, withdraw_amount):
        if self.balance < withdraw_amount:
            print('Insufficient funds.')
        else:
            self.balance -= withdraw_amount
        
    def account_balance(self):
        return f'Your current balance is ${self.balance}'


class SavingsAccount:
    pass