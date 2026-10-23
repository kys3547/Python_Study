# LeetCode
# 70. Climbing Stairs

"""
Instruction

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        fn2 = 0
        fn1 = 1
        i = 0

        while i < n:
            fn = fn2 + fn1
            fn2 = fn1
            fn1 = fn
            i += 1

        return fn

solution = Solution()

print("Case1, n = 2:\t", solution.climbStairs(2))
print("Case2, n = 3:\t", solution.climbStairs(3))
print("Case3, n = 45:\t", solution.climbStairs(45))