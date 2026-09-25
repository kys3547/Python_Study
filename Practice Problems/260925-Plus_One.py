# LeetCode
# 66. Plus One

"""
Instruction

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
"""

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = 0

        for i in range(len(digits)):
            num += digits[i] * 10 ** (len(digits) - 1 - i)
        
        num += 1

        numList = [int(j) for j in str(num)]

        return numList

solution  = Solution()

print("Case 1 [1, 2, 3]:\t", solution.plusOne([1, 2, 3]))
print("Case 2 [4, 3, 2, 2]:\t", solution.plusOne([4, 3, 2, 2]))
print("Case 3 [9]:\t\t", solution.plusOne([9]))