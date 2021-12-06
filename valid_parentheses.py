# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 


class Solution:
    def isValid(self, s: str) -> bool:
        val={')':'(', ']':'[', '}':'{'}
        stack=[]
        for char in s:
            if char in val.values():
                stack.append(char)
            else:
                if stack!=[] and stack.pop()==val[char]:
                    continue
                else:
                    return False
        if stack:
            return False
        else:
            return True