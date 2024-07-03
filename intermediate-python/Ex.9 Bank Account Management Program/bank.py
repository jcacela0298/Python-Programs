"""
Author: Jack Cacela
File: bank.py
This module defines the Bank class. The bank class imports the savingsaccount.py file as 
a dependency, and allows the user to add and remove accounts, compute the interest of all 
accounts, save the accounts to a pickled .bar file, and retrieve information from one account 
or all accounts. 
"""

from savingsaccount import SavingsAccount
import pickle

class Bank(object):
   
    def __init__(self, fileName = None):
        """Creates a new dictionary to hold the accounts. If a filename is provided, loads the 
        accounts from a .bar file of pickled accounts, or creates a new, empty bank if the filename 
        is not present."""
        self.accounts = {}
        self.fileName = fileName
        if fileName != None:
            fileObj = open(fileName, "rb") # rb stands for "read binary" which is pickle-specific.
            while True:
                try:
                    account = pickle.load(fileObj) # This attempts to load a pickled object from fileObj. 
                    # The pickle.load() function reads the next object from the file and deserializes it.
                    self.add(account) # This adds the loaded account (which is an instance of SavingsAccount) 
                    # to the accounts dictionary of the Bank instance using the bank's add method.
                except EOFError:
                    fileObj.close() # Closes the file fileObj after all accounts have been loaded or when an 
                    # EOFError occurs. This is important to release system resources associated with the file.
                    break # Breaks out of the while True loop once all accounts have been loaded from the file. 
                    # This ensures that the loading process stops when the end of the file is reached (EOFError)

    def __str__(self):
        """Return the string representation of the entire bank."""
        # Here, map(str, self.accounts.values()) applies the str function to each 
        # SavingsAccount instance stored in self.accounts.values().
        # This effectively calls the __str__ method of each SavingsAccount instance,
        # aka each object of type SavingsAccount, so it prints the information of each account.
        return '\n'.join(map(str, self.accounts.values())) 

    def makeKey(self, name, pin): 
        """Makes and returns a key from name and pin. The makeKey method constructs a string that uniquely identifies each account 
        (which is the key's value, aka each SavingsAccount object) in the Bank's accounts dictionary. This string is used as a key 
        to access and manage individual accounts within the dictionary."""
        return name + "/" + pin

    def add(self, account):
        """Inserts an already-made account with name and pin as a key into the accounts dictionary."""
        key = self.makeKey(account.getName(), account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):
        """Removes an account with name and pin as a key."""
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None) # Here, "None" is a second parameter that indicates that the account was not found in the bank,
        # and thus nothing was "popped" or removed, since there was no key in the dictionary.

    def get(self, name, pin):
        """Normally, The built-in get() method in Python dictionaries serves a general-purpose function to 
        retrieve values based on keys. In this Bank class, the get() method serves a specific purpose tailored 
        to this application's needs, which is to do the same thing and return an account, but making sure it accepts
        a name and pin as a key, and returns None if not found. """
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None) # Here, "None" indicates that the given account is not in the bank.

    def computeInterest(self): #confused what this method does. Does it add up all the interest money in all accounts?
        """Computes the simplified interest (from the savingsaccount.py method "computeInterest" for each account and 
        returns the total."""
        total = 0.0
        for account in self.accounts.values():
            total += account.computeInterest()
        return total

    def save(self, fileName = None):
        """Saves all accounts in the bank to a file and pickles each account. The parameter
        allows the user to change filenames to change where to save the accounts."""
        if fileName != None:
            self.fileName = fileName
        elif self.fileName == None:
            return
        fileObj = open(self.fileName, "wb")
        for account in self.accounts.values():
            pickle.dump(account, fileObj) # Serializes (pickles) the current account object and writes it to fileObj
        fileObj.close() # Closes the file object after all accounts have been serialized and saved.