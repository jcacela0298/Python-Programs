""" 
File: company.py
Defines classes for a Customer and an Employee using inheritance and overriding.
"""


from person import Person


class Customer(Person):
    """Represents a customer."""
    
    def __init__(self, name, address, phone, credit_score):
        """Constructor creates a customer with the given
        name, address, phone number, and credit score."""
        Person.__init__(self, name, address, phone)
        self.credit_score = credit_score

    def get_credit_score(self):
        """Returns the customer's credit score."""
        return self.credit_score

    def set_credit_score(self, credit_score):
        """Sets the customer's credit score."""
        self.credit_score = credit_score

    def __str__(self):
        """Returns the string representation of the customer."""
        return "Name: " + self.name + \
               "\nAddress: " + self.address + \
               "\nPhone: " + self.phone + \
               "\nCredit Score: " + str(self.credit_score)


class Employee(Person):
    """Represents an Employee."""
    
    def __init__(self, name, address, phone, badge, salary):
        """Constructor creates an employee with the given
        name, address, phone number, badge number, and salary."""
        Person.__init__(self, name, address, phone)
        self.badge = badge
        self.salary = salary

    def get_badge(self):
        """Returns the employee's badge number."""
        return self.badge

    def set_badge(self, badge):
        """Sets the employee's badge number."""
        self.badge = badge

    def get_salary(self):
        """Returns the employee's salary."""
        return self.salary

    def set_salary(self, salary):
        """Sets the employee's salary."""
        self.salary = salary

    def __str__(self):
        """Returns the string representation of the employee."""
        return "Name: " + self.name + \
               "\nAddress: " + self.address + \
               "\nPhone: " + self.phone + \
               "\nBadge: " + str(self.badge)

    def __eq__(self, other):
        """Includes the equals method, overriding it for this progam to compare badge numbers."""
        if isinstance(other, Employee):
            return self.badge == other.badge
        return False