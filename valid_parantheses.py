"""
iven a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

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

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false


"""
from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        valid_bracket={
            ')':'(',
            '}':'{',
            ']':'['

        }
        stack=[]
        for bracket in s:
            # print("bracket is : ", bracket )
            if bracket in valid_bracket :
                # print("before pop :- ",stack)
                if stack and stack[-1] == valid_bracket[bracket]:
                    stack.pop()
                    # print("post pop :- ",stack)
                else:
                    return False
            else:
                    stack.append(bracket)
                    # print("post append :" , stack)
        return len(stack) == 0
object = Solution()
print(object.isValid("()[]{}"))