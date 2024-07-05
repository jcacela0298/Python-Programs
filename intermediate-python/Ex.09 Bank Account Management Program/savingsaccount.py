"""
Author: Jack Cacela
File: savingsaccount.py
This module defines the SavingsAccount class, which provides the methods to add
accounts with a name, a pin number, and a balance, and also allows one to
deposit and withdraw money, compute the interest, and retrieve the account information.
"""

class SavingsAccount(object):
    """This class represents a savings account with the owner's name, PIN, and balance."""
    
    RATE = 0.02  # Single rate for all accounts
    
    def __init__(self, name, pin, balance=0.0):
        # Variables that begin with "self" are instance variables that can be 
        # modified in each method of the SavingsAccount class. 
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        """Returns the neat string representation."""
        result = 'Name: ' + self.name + '\n'
        result += 'PIN: ' + self.pin + '\n'
        result += 'Balance: ' + str(self.balance)
        return result

    def getBalance(self):
        """Returns the current balance."""
        return self.balance

    def getName(self):
        """Returns the current name."""
        return self.name

    def getPin(self):
        """Returns the current pin."""
        return self.pin

    def deposit(self, amount):
        """Deposits the given amount and returns None."""
        self.balance += amount
        return None

    def withdraw(self, amount):
        """Withdraws the given amount.
        Returns None if successful, or an error message if unsuccessful."""
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None

    def computeInterest(self):
        """Computes, deposits, and returns the interest. In real-world scenarios,
        interest accrual and compounding usually occur over time periods like months 
        or years. However, the computeInterest method in this simplified example 
        immediately calculates and adds the interest to the balance before returning."""
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest