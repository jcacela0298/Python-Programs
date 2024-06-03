"""
Program: Phone Number Finder
Author: Jack Cacela
Date: 2024-06-03

When the user enters either a last name, or a first and last name,
This program finds the corresponding first name, last name,
and phone number from the phones.txt file, and returns the 
information in the following format:
<first name> <last name>, <phone number>
and keeps asking the user for names until the user enters 
an empty or blank line.

Input: The last name, or a first and last name, of an individual(s)
Output: The first name, last name, and phone number of the individual(s).
"""

# Main loop
while True:
    
    # Collect user input while removing leading or trailing whitespaces and converting to lowercase
    user_input = input("Enter a last name, or first and last name: ").strip().lower()
    
    # Exit if the user enters an empty line
    if user_input == "":
        break
    
    # Split the input string into a list of words
    input_parts = user_input.split()
    
    # Check for invalid input (more than two names)
    if len(input_parts) > 2:
        print("Error: Only enter a last name or a first and last name.")
        # Prompt the user for more input via continue instead of exiting program via break
        continue
    
    # Open the file for reading and search for matching names
    f = open("phones.txt", 'r')
    
    # Initialize the found_match variable outside the loop as a flag to see if a match is found
    found_match = False
    
    # Each iteration of this upcoming loop reads one line from the file until it encounters a newline 
    # character, at which point it knows it has reached the end of the current line and moves 
    # on to the next one for the next iteration of the loop
    for line in f:
        
        # Manually split each line from phones.txt by spaces into first name, last name, and phone number,
        # again removing any trailing or leading white spaces
        parts = line.strip().split()
        first_name = parts[0].lower()
        last_name = parts[1].lower()
        phone_number = parts[2]
        
        # Check for file matches for the two words that were entered by the user
        if len(input_parts) == 2:
            if first_name == input_parts[0] and last_name == input_parts[1]:
                print(f"{parts[0]} {parts[1]}, {parts[2]}") # f-string to include the comma
                found_match = True
              
        # Check for file matches for the one word that was entered by the user
        elif len(input_parts) == 1:
            if last_name == input_parts[0]:
                print(f"{parts[0]} {parts[1]}, {parts[2]}") # f-string to include the comma
                found_match = True

    # If no matches were found, print "No match found."
    if not found_match:
        print("No match found.")
        
# Close the file once finished    
f.close()

# Exit the program message
print("Exiting...")