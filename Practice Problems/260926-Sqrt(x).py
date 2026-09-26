# LeetCode
# 69. Sqrt(x)

"""
Instruction

Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        right = x
        left = 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid < x:
                temp = mid
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid

        return temp

solution = Solution()

print("Case 1, x = 4:\t", solution.mySqrt(4))
print("Case 2, x = 8:\t", solution.mySqrt(8))

"""
Note

Use while loop, start from i = 1, compare i ** 2 and x. get the closest value
This will probably the worst answer possible, but lets give it a try

1st Attempt:
import sys

class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        temp = sys.maxsize

        while True:
            if (x > (i * i)) and (x < ((i + 1) * (i + 1))) or x == (i * i):
                return i
            else:
                i += 1

RESULT
Runtime: 3351ms, beats 5.05%
Memory: 19.30MB, beats 55.80%

Pathetic! There must be a better answer.


"""