# LeetCode
# 112. Path Sum

"""
Instruction

Given the root of a binary tree and an integer targetSum,
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.
"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val

        remaining = targetSum - root.val

        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)

"""
Notes

I don't understand...

So when root is None, it means there is no match (with targetSum). So retrun False.
If root is a leaf node and if remaining is equal to targetsum - root.val, it returns targetsum == root.val


"""