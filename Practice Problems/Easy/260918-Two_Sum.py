# LeetCode
# 1. Two Sum
"""
Description:
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)): # i in range of [0, 3]
        for j in range(len(nums)): # j in range of [0, 3]
            if (nums[i] + nums[j] == target) and i != j:
                return [i, j]
    return []

print("Case 1:", twoSum([2, 7, 11, 15], 9))
print("Case 2:", twoSum([3, 2, 4], 6))
print("Case 3:", twoSum([3, 3], 6))

# Note
"""
I got it wrong at first because I was not checking if i != j.
I got it wrong at the second time because I was using 'for i in nums' and 'for j in nums.'
I was using 'nums.index(i) != nums.index(j)' to compare the indices,
but index() returns the first index of the value.
So in Case 3, 'nums.index(i) != nums.index(j)' would always return False because
both i and j are 3, so 'nums.index(i)' and 'nums.index(j)' would both return 0.

I used 'range(len(nums))' to fix the problem.
Instead of using values of the list, I used the indices of the list to compare them.

---Better Solution---
def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# in this case, there's no need to check i != j because j is always greater than i. 
"""