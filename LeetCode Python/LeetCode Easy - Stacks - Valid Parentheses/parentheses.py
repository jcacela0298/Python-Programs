class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determine if the input string `s` containing just the characters '(', ')', '{', '}', '[' and ']'
        is a valid string of parentheses. A string is valid if:
        - Open brackets are closed by the same type of brackets.
        - Open brackets are closed in the correct order.
        - Every close bracket has a corresponding open bracket of the same type.
        
        Args:
        s (str): The input string containing only the characters '(', ')', '{', '}', '[' and ']'.

        Returns:
        bool: True if the input string is valid, False otherwise.
        """
        
        # Initialize an empty stack to keep track of opening brackets
        stack = []
        
        # Dictionary to map each closing bracket to its corresponding opening bracket
        closeToOpen = { ")" : "(", "]" : "[" , "}" : "{" }

        # Iterate over each character in the input string
        for c in s:
            # Check if the character is a closing bracket
            if c in closeToOpen:
                # Check if the stack is not empty and the top element of the stack
                # matches the corresponding opening bracket for the current closing bracket
                if stack and stack[-1] == closeToOpen[c]:
                    # Remove the matching opening bracket from the stack
                    stack.pop()
                else:
                    # If there's no matching opening bracket or the stack is empty,
                    # the string is invalid
                    return False
            else:
                # If the character is an opening bracket, push it onto the stack
                stack.append(c)

        # If the stack is empty, all brackets were matched correctly, return True
        # Otherwise, return False as there are unmatched opening brackets
        return True if not stack else False