# LeetCode
# 94. Binary Tree Inorder Traversal

"""
Instruction

Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        else:
            lresult = self.inorderTraversal(root.left)
            rresult = self.inorderTraversal(root.right)

            return lresult + [root.val] + rresult

"""
Note

Inorder: visit left subtree entirely -> visit this node -> visit right subtree entirely
When root is none, return nothing.
When root is not none, call inorderTraversal on root.left and root.right. Store their results.

Combine all three results and return
"""