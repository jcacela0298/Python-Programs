from bank import Bank 
from savingsaccount import SavingsAccount 
# Even though bank.py imports SavingsAccount, the definitions 
# (classes, functions, variables) from savingsaccount.py are only 
# available within bank.py unless explicitly imported elsewhere, hence
# why we need to import savingsaccount here.



# Create a bank object and add accounts
bank = Bank()
bank.add(SavingsAccount("Wilma", "1001", 4000.00))
bank.add(SavingsAccount("Fred", "1002", 1000.00))

# Print the bank
print("Bank after adding these accounts:")
print(bank) # Calls the __str__ method of Bank on the object

# Get an account with wrong PIN (should return None)
account = bank.get("Wilma", "1000")
print("\nAccount with incorrect PIN (should be None):")
print(account) # Calls the __str__ method of SavingsAccount on the object

# Get an account with correct PIN
account = bank.get("Wilma", "1001")
print("\nAccount with correct PIN:")
print(account)

# Deposit money into the account
account.deposit(25.00)
print("\nAccount after depositing 25.00:")
print(account)

# Print the bank after deposit
print("\nBank after deposit:")
print(bank)


# Save the bank to a file -- After calling this bank.save("bank.dat") method, you will 
# have a file named bank.dat in the current working directory. This file contains 
# the pickled (serialized) account objects from your Bank instance
bank.save("bank.dat")


# Create a new bank object and load accounts from the recently added bank.dat file with the 
# recently added accounts, where the __init__ method will then unpickle (deserialize) the
# account objects, and add them to the new Bank instance:
new_bank = Bank("bank.dat")
print("\nNew bank loaded from file:")
print(new_bank)

# Wait for user input before exiting
input("Press Enter to exit...")