# LeetCode
# 9. Palindrome Number

"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
Constraints:
-231 <= x <= 231 - 1
 
Follow up: Could you solve it without converting the integer to a string?
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False # all negative numbers are not palindromes
        else:
            return str(x) == str(x)[::-1]

"""
# Different Solution

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        halfRev = 0

        while halfRev < x:
            halfRev = halfRev * 10 + (x % 10)
            x //= 10

        return halfRev == x or halfRev // 10 == x
"""

solution = Solution()
print("Is 121 a palindrome?\t", solution.isPalindrome(121))
print("Is -121 a palindrome?\t", solution.isPalindrome(-121))
print("Is 10 a palindrome?\t", solution.isPalindrome(10))
