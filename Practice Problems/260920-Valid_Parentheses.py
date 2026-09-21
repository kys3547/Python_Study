# LeetCode
# 20. Valid Parentheses

"""
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

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        stack = []

        for i in range(len(s)):
            if s[i] in mapping: stack.append(s[i])
            else:
                if not stack:   return False
                else:
                    if mapping[stack.pop()] != s[i]: return False
        
        return not stack

solution = Solution()

print("Case 1, ():\t", solution.isValid("()"))
print("Case 2, ()[]{}:\t", solution.isValid("()[]{}"))
print("Case 3, (]:\t", solution.isValid("(]"))
print("Case 4, ([]):\t", solution.isValid("([])"))
print("Case 5, ([)]:\t", solution.isValid("([)]"))

"""
Note

It was very difficult to approach. I first tried to make a copy list of 's' and remove all the coupling parentheses.
So I read through the copy using for loop and if I find an opening parentheses,
I used index method to find a matching closing parentheses. By subtracting the index of opening from the index of closing
and getting a remainder, I can figure out that there's no lonely parentheses between two of them.

This approach was obviously wrong. If there are an odd number of unmatched parentheses b/w a pair of matched parentheses(just like [}}(]),
the algorithm will consider the matched one as unmatched one. Besides, it is too complicated.

I did some research, and developed another algorithm. This mimics stack datatype(which Python does not have).
First I created an empty list named stack. Then I used a for loop to go through each character.
If it finds an opening parentheses, the parentheses is stored in a stack list using append method.
If there is an closing parentheses, first the algorithm checks if the stack is empty or not.
If empty, it returns False, because it means that there's no match.
If not, it compares the last element of stack using pop method and see if they are a match. If not, it returns False.

At the end, if everything went correctly, there will be no elements left in stack. So the code returns not stack.
"""