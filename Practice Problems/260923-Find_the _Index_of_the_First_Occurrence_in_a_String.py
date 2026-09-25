# LeetCode
# 28. Find the Index of the First Occurrence in a String

"""
Instruction

Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

"""
Note

I feel like the answer's illegal. Just use .find and done? Can't be. Guess there's more elegant answer.
I will look up the hint

I found a different solution in LeetCode Community:

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        
        return -1

This guy claims that he beated 100% with this answer. So let's think.

Aha! get it

So the reason why i iterates through range(len(haystack) - len(needle) + 1) is to make sure that there's
enough space for needle to fit.

For example, let's say the given haystack is "sadbutsad" and needle is "sad". 
In this case, the last index that needle can fit is 9 - 3 = 6, which is equal to. len(haystack) - len(needle).
Since range() is exclusive at the end, 1 must be added.

haystack[i: i + len(needle)] -> slices haystack from i to length of needle.

Okay I understood

Reminder of String slicing
str[start:end] -> from start to end. (end is exclusive)
str[:end] -> from the beginning of the str to end
str[start:] -> from start to the end of the str
str[start:end:step] -> from start to end, but only gets every (step)th character
use negative index to start from the end
"""