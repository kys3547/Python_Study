# LeetCode
# 111. Minimum Depth of Binary Tree

"""
Instruction

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

"""
Notes

When root is None, return 0. When root.left is None, move on to root.right and vice versa.
At the end, return the minimum value of root.left and right + 1(including root itself).
"""