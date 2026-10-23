# LeetCode
# 125. Valid Palindrome

"""
Instruction

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanTxt = []
        s = s.lower()

        for ch in s:
            if ch.isalnum():
                cleanTxt.append(ch)

        
        return cleanTxt == cleanTxt[::-1]