# Python Sorter Program

I built a program that accepts two or more strings from the command line and displays them sorted alphabetically by each string's first character.

To run this program, navigate to the correct directory, and then type 
    Python jack_sort.py
After doing so, enter in 2 or more strings such as: apples bananas cherries

During this project, I learned more about overall Python syntax, how to import modules, how to collect user data, if / else conditions, how "len" can refer to the number of "words" for my input strings parameter: 

if len(input_strings) < 2:

How to use the sorted function with this function's specific key words, and how to join components in a list variable into a string by doing this:

 sorted_list_as_string = ' '.join(sorted_strings)

 print("Sorted strings:", sorted_list_as_string)