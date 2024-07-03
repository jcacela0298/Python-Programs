Features:


This program features the advanced topics of the Python class / object paradigm including dependencies, instance variables, class variables, getters, setters, __str__, __init__, docstrings, module naming conventions, using a test file, and pickling.

The savingsaccount.py file with the SavingsAccount class provides the methods to add accounts with a name, a pin number, and a balance, and also allows one to deposit and withdraw money, compute the interest, and retrieve the account information.

The bank.py file with the Bank class imports the savingsaccount.py file as a dependency, and allows the user to add and remove accounts, compute the interest of all accounts, save the accounts to a pickled .bar file, and retrieve information from one account or all accounts. 



Usage:

To use this program, run the "test.py" file, and observe in the "demo.txt" file the results of the print statements from the "test.py" file to observe the method functionality. Also, feel free to re-run the test.py file with your own values -- below are the methods for each module.


Savings Account Methods				Description


a = SavingsAccount(name, pin, balance = 0.0)	Returns a new account with the given name, PIN, and balance.

a.deposit(amount)				Deposits the given amount to the account’s balance.

a.withdraw(amount)				Withdraws the given amount from the account’s balance.

a.getBalance()					Returns the account’s balance.

a.getName()					Returns the account’s name.

a.getPin()					Returns the account’s PIN.

a.computeInterest()				Computes the account’s interest and deposits it.

a.__str__()					Same as str(a). Returns the string representation of the account.



Savings accounts most often make sense in the context of a bank. A very simple bank allows a user to add new accounts, remove accounts, get existing accounts, and compute interest on all accounts. A Bank class thus has these four basic operations (add, remove, get, and computelnterest) and a constructor:


Bank Method					Description


b = Bank()					Returns a bank.

b.add(account)					Adds the given account to the bank.

b.remove(name, pin)				Removes the account with the given name and pin from the bank and returns the account. If the account is not in the bank, returns None.

b.get(name, pin)				Returns the account associated with the name and pin if it’s in the bank. Otherwise, returns None.

b.computeInterest()				Computes the interest on each account, deposits it in that account, and returns the total interest.

b.__str__()					Same as str(b). Returns a string representation of the bank (all the accounts).

b.save("bank.dat")				Saves and pickles the bank accounts into the binary bank.dat file





Example:

(See the test.py file, and the demo.txt file includes the results of the test.py file)
