# LeetCode
# 35. Searh Insert Position

"""
Instruction

Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while right >= left:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return left

"""
Note

So this problem wants me to use binary search, which I almost forgot.
First, get the middle value of nums and compare it with target.
if target is bigger than middle, no need to loop the first half
if target is smaller than middle, no need to loop the second half

remove the unneccessary ones and I will get target at the end.

Binary Search (Search Insert Position)

- Keep nums untouched; never slice it. Instead, track the current
  search range with two index variables, left and right, so the
  original indices are never lost.
- Recalculate mid = (left + right) // 2 every iteration, since
  left/right change each time the range narrows.
- Loop condition is `while right >= left`, not `!=`. left can
  overshoot right by exactly one step when the target isn't found,
  so `>=` is needed to catch that case and stop the loop.
- If nums[mid] > target: narrow to the left half (right = mid - 1)
- If nums[mid] < target: narrow to the right half (left = mid + 1)
- If nums[mid] == target: found it, mid is the answer

- If the loop exits without finding target, left and right have
  crossed: right points to the last value smaller than target,
  and left points to the first value greater than target.
  So `left` is exactly the correct insert position -> return left.

"""