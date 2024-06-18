"""
Program: Lookup
Author: Jack Cacela

This program allows users to look up phone numbers or addresses from the address.txt data file.
Once the user selects their preferred type of lookup, the program will prompt for a person's
name (first and last) and display the corresponding information if found. 

Input:
    User input:
    - Choice (1 or 2) for phone numbers or addresses lookup.
    - First and last name of the person to look up.

Output:
    Depending on the user's choice:
    - Phone number(s) in the format 'Phone: xxx-xxx-xxxx'.
    - Address information in the format:
        Street: [street name]
        City: [city name]
        State: [state abbreviation]
        Zip Code: [zip code]

The data file 'address.txt' is used to store information in comma-separated format:
[first and last name], [street], [city], [state], [zip code], [phone number].

Note:
- Names are case-insensitive when searching.
- Proper error handling is implemented for file not found and invalid user input.
"""



# Import sys for error handling
import sys



def main():

    # Call the input_addresses function to populate the address/phone dictionary
    info_dict = input_addresses()
    
    # Ask the user if they want to lookup phone numbers or addresses, 
    # Making sure to strip any leading and trailing spaces from their input
    while True:
        choice = input("Lookup (1) phone numbers or (2) addresses: ").strip()
        
        # Check for an empty string before converting choice to an integer
        if choice == "": 
            break
        
        # Convert input string to an integer, and then pass that integer as well as the dictionary to the output function
        try:
            choice = int(choice)
            if choice == 1:
                output(info_dict, display=1)
            elif choice == 2:
                output(info_dict, display=2)
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid choice. Please enter 1 or 2.")

    

#**************************************************************
# Function: input_addresses 
# 
# Purpose: Stores the information from the address.txt file into 
# a dictionary called the_dictionary, creating key value pairs 
# where the first and last name is the key, and the value is the 
# rest of the line associated with the first and last name.
#          
# Parameters: void
# 
# Returns:
#
#    the_dictionary - The completed dictionary 
#  
#**************************************************************    

def input_addresses():

    # Create a dictionary
    the_dictionary = {}

    # Read the address.txt file into the dictionary, with error handling in case file is not found
    try:
        f = open("address.txt", 'r')
        for line in f:
            parts = line.strip().split(",") # Divide each line into a stripped list separated by commas, and store into the parts variable
            first_last = parts[0].strip().lower()  # First and last name combined as the key
            the_dictionary[first_last] = line.strip()  # Setting the rest of the line as the value
        f.close()

    except FileNotFoundError:
        print("Error: the file 'address.txt' was not found.")
        sys.exit(1) # Exit the program if the file is not found

    return the_dictionary # Return the completed dictionary back to the calling function



#**************************************************************
# Function: output 
# 
# Purpose: Collects the requested first and last name from the user
# and returns the information in the specified format from the dictionary. 
#          
# Parameters: 
#               info_dict - The completed dictionary.
#               display - the value, 1 or 2, as selected by the user,
#                         and the default is set to 1.
# 
# Returns:
#
#    prints the information in the format that the user requests.
#  
#**************************************************************  

def output(info_dict, display=1):

    # Convert the user input to lower case and remove any leading and trailing spaces
    name = input("Enter space-separated first and last name: ").strip().lower()
    
    # If the name is in the dictionary, store the value (an entire line) of that key (the name) into the info variable
    if name in info_dict:
        info = info_dict[name]
        if display == 1:
            # If the user selected 1, split info into a list separated by commas, 
            # and retrieve the -1 (last) index position, which is the phone number
            phone_number = info.split(",")[-1].strip()  
            print(f"Phone: {phone_number}")
        elif display == 2:
            # If the user selected 2, split info into a list separated by commas,
            # and extract other address details from the split info list
            parts = info.split(",")
            street = parts[1].strip()
            city = parts[2].strip()
            state = parts[3].strip()
            zip_code = parts[4].strip()
            print(f"Street: {street}")
            print(f"City: {city}")
            print(f"State: {state}")
            print(f"Zip Code: {zip_code}")
    else:
        print("Error: person not found.")



# When you run this script directly from terminal or the command line, __name__ is set to "__main__", 
# which makes this below statement true, so the main() function from this script is called.
# However, if you import this script as a module into another script, __name__ becomes equal to the name of the other script
# That it is being imported into, so that main() from this script does not automatically run when the other script is run.
# The reason for this is so that if imported into another script, functions from this current script may
# Be used within the other script, without the main() function from this script activating and interfering with the other script.
if __name__ == "__main__":
    main()