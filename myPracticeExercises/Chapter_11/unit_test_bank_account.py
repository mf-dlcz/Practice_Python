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
        return f"Account Number: {self.account_number} Balance: ${round(self.balance, 2):.02f}"
        

class SavingsAccount(Account):
    
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        self.balance += (self.balance * self.interest_rate) / 12
        
    def summary(self):
        return f"{super().summary()} Interest Rate: {self.interest_rate}"


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

    def test_withdraw_underdraft(self):
        account = Account(123456, 100)
        account.withdraw(-100)
        self.assertEqual(account.balance, 100)

    def test_get_balance(self):
        account = Account(123456, 100)
        self.assertEqual(account.get_balance(), 100)
        account.deposit(1000)
        self.assertEqual(account.get_balance(), 1100)
        account.withdraw(1000)
        self.assertEqual(account.get_balance(), 100)

    def test_summary(self):
        account = Account(123456, 250)
        expected = 'Account Number: 123456 Balance: $250.00'
        self.assertEqual(account.summary(), expected)

class TestSavingsAccountClass(unittest.TestCase):

    def setUp(self):
        # account_number, balance, interest_rate
        self.ACCOUNT_NUMBER = 2048
        self.INITIAL_DEPOSIT = 2500
        self.INTEREST_RATE = 0.024
        self.account = SavingsAccount(self.ACCOUNT_NUMBER, self.INITIAL_DEPOSIT, self.INTEREST_RATE)

    def test_constructor(self):
        self.assertEqual(self.account.account_number, str(self.ACCOUNT_NUMBER))
        self.assertEqual(self.account.balance, self.INITIAL_DEPOSIT)
        self.assertEqual(self.account.interest_rate, self.INTEREST_RATE)

    def test_interest_rate_set(self):
        pass

    def test_apply_interest(self):
        self.account.apply_interest()
        expected_balance = 2505.00  # 2500 + (2500 * 0.024) / 12 = 2500 + 5.0
        actual = self.account.balance
        self.assertEqual(actual, expected_balance)

    def test_summary(self):
        self.account.apply_interest()
        expected_summary = 'Account Number: 2048 Balance: $2505.00 Interest Rate: 0.024'
        actual_summary = self.account.summary()
        self.assertEqual(actual_summary, expected_summary)

if __name__ == '__main__':
    unittest.main(verbosity = 2)