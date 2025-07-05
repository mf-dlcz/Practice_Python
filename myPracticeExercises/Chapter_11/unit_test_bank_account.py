"""
Modify the accounts.py program from the section on Classes and Objects by adding unit tests for 
the Account and SavingsAccount classes.
Verify the following: 
    - The constructor for each class assigns all values correctly
    - Methods return the proper values or modify other member variables appropriately
"""

import unittest
from pprint import pprint

class Account:
    
    def __init__(self, account_number, balance):
        self.account_number = str(account_number)
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount < 0:
            return
        self.balance -= amount
    
    def get_balance(self):
        return self.balance
    
    def summary(self):
        return f"Account Number: {self.account_number} Balance: ${round(self.balance, 2)}"
        

class SavingsAccount(Account):
    
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    
    def apply_interest(self):
        self.balance += (self.balance * self.interest_rate) / 12
        
    def summary(self):
        return f"{super().summary()} Interest rate: {self.interest_rate}"


####             UNIT TEST               ####


class TestAccountClass(unittest.TestCase):

    def test_constructor(self):
        account = Account(account_number = 123456 , balance = 0)
        self.assertEqual(account.account_number, '123456')
        self.assertEqual(account.balance, 0)

    def test_deposit(self):
        account = Account(123456, 0)
        account.deposit(11.04)
        self.assertEqual(account.balance, 11.04)

    def test_withdraw(self):
        account = Account(123456, 11.04)
        account.withdraw(5.00)
        self.assertAlmostEqual(account.balance, 6.04)

    def test_get_balance(self):
        pass

    def test_summary(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity = 2)