This program returns true if a string filled with opening and closing parentheses / brackets / curly braces is "valid" based on the program summary below. 

To run this program, run the test_parentheses.py file and confirm that the parentheses tester works. Feel free to change the input in the test file and verify that the program works.



Program summary:

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.