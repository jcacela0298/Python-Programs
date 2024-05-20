#!/usr/bin/python

# Assignment 3
# Jack Cacela and Spencer Marks
# This Python program accepts 2 or more strings from the command line and displays them sorted alphabetically by each string's first character.

# To run this program, navigate to the correct directory, and type Python jack_sort.py
# After doing so, enter in 2 or more strings such as: apples bananas cherries
 
import sys
# The sys module, while fairly common, is not actually used in this program. This did, however, teach me the syntax of how to import modules.

input_strings = input("Enter two or more words separated only by spaces: ").split()

if len(input_strings) < 2:
    print("Please enter two or more words to sort.")
else:
    sorted_strings = sorted(input_strings, key=lambda s: s[0].lower())
   
    sorted_list_as_string = ' '.join(sorted_strings)
    print("Sorted strings:", sorted_list_as_string)
