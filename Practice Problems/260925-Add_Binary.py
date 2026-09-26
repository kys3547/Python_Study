# LeetCode
# 67. Add Binary

"""
Instruction

Given two binary strings a and b, return their sum as a binary string.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a, 2)
        num2 = int(b, 2)

        return bin(num1 + num2)[2:]

solution = Solution()

print("Case 1\t\t11 + 1 = ", solution.addBinary("11", "1"))
print("Case 2\t\t1010 + 1011 = ", solution.addBinary("1010", "1011"))