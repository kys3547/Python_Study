# LeetCode
# 88. Merge Sorted Array

"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        end1 = m - 1        # end of real values in nums1
        end2 = n - 1        # end of real values in nums2
        current = m + n - 1 # end of the entire list

        while end1 >= 0 and end2 >= 0:
            if nums1[end1] > nums2[end2]:
                nums1[current] = nums1[end1]
                end1 -= 1
            else:
                nums1[current] = nums2[end2]
                end2 -= 1

            current -= 1

        while end2 >= 0:
            nums1[current] = nums2[end2]
            end2 -= 1
            current -= 1