"""
File: person.py
Author: Jack Cacela
This is the blueprint for creating a person for the identification program.
"""


class Person(object):
    """ Defines information for a person """
    
    def __init__(self, name, address, phone):
        """Constructor creates a person with the given
        name, address, and phone number"""
        self.name = name
        self.address = address
        self.phone = phone

    def set_address(self, address):
        """Sets the person's address."""
        self.address = address

    def get_address(self):
        """Returns the person's address."""
        return self.address
    
    def set_phone(self, phone):
        """Sets the person's phone number."""
        self.phone = phone

    def get_phone(self):
        """Returns the person's phone number."""
        return self.phone

    def get_name(self):
        """Returns the person's name."""
        return self.name

    def __str__(self):
        """Returns the string representation of the person"""
        return "Name: " + self.name + \
               "\nAddress: " + self.address + \
               "\nPhone: " + self.phone
