# LeetCode
# 145. Binary Tree Postorder Traversal

"""
Instruction

Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""

class TreeNode:
    def __init___(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        
        else:
            lresult = self.postorderTraversal(root.left)
            rresult = self.postorderTraversal(root.right)

            return lresult + rresult + [root.val]