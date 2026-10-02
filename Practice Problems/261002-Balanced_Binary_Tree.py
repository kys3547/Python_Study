# LeetCode
# 110. Balanced Binary Tree

"""
Instruction

Givn a binary tree, determine if it is height-balanced.
"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def checkDepth(root: TreeNode | None) -> int:
            if not root:
                return 0
    
            left = checkDepth(root.left)
            if left == -1:
                return -1
            
            right = checkDepth(root.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1  
    
            return max(left, right) + 1

        return checkDepth(root) != -1

"""
Notes

I recycled maxDepth from previous problem, but modified it to return -1 whenever it detects an unbalance.
"""