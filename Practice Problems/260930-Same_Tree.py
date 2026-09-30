# LeetCode
# 100. Same Tree

"""
Instruction

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.
"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True
        elif (p is None) ^ (q is None):
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val

"""
Note

1st attempt:
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        def traverse(root: TreeNode | None) -> list[int]:
            if root is None:
                return []
            else:
                lres = traverse(root.left)
                rres = traverse(root.right)
                return lres + [root.val] + rres

        if traverse(p) == traverse(q):
            return True
        else:
            return False

This approach is unable to get the currect answer when the trees are only consisted of None and same numbers.
It's because None is removed in the process of converting a tree into a list.
Probably better to compare them without converting into a list.
"""