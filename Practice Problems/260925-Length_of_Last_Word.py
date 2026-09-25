# LeetCode
# 58. Length of Last Word

"""
Instrunction

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        i = len(s) - 1 # the index of the end of s

        while i >= 0:
            if s[i] == " ":
                return len(s) - 1 - i
            else:
                i -= 1

        return len(s)

solution = Solution()

print("Case 1, \'Hello World\':\t\t\t", solution.lengthOfLastWord("Hello World"))
print("Case 2, \'   fly me   to   the moon  \':\t", solution.lengthOfLastWord("   fly me   to   the moon  "))
print("Case 2, \'luffy is still joyboy\':\t", solution.lengthOfLastWord("luffy is still joyboy"))