# LeetCode
# 144. Binary Tree Preorder Traversal

"""
Instruction

Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""

class TreeNode:
    def __init___(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
                    return []
        
        else:
            lresult = self.preorderTraversal(root.left)
            rresult = self.preorderTraversal(root.right)

            return [root.val] + lresult + rresult

"""
Notes

I refered to 260930-Binary Tree Inorder Traversal.py -> changed the output order to val, left, right
"""