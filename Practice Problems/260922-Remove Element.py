# LeetCode
# 27. Remove Element

"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = len(nums)
        i = 0

        while i < k:
            if nums[i] == val:
                k -= 1
                nums[i] = nums[k]
                if nums[i] != val:
                    i += 1
            else:
                i += 1

        return k
"""

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

"""
Note

Using two pointers is hard... I always have no clue until I see hints.
My first soolution uses two pointers but one pointer starts at the end of the list.
So the solution got quite complicated, and it looks dirty.

The second solution uses two pointers, but this time both of them starts from
the beginning of the list. When it encounters val, the writing pointer stays.
The reading pointer continues and search for non-vals. Once found, it replaces
val(k) with non-val(i)
"""