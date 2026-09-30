# LeetCode
# 101. Symmetric Tree

"""
Instruction

Given the root of a binary tree check whether it is a mirror f itself (i.e., symmetric around its center)
"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isMirror(self, p: TreeNode | None, q: TreeNode | None) -> bool:
            if p is None and q is None:
                return True
            elif (p is None) ^ (q is None):
                return False
            
            return self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left) and p.val == q.val

    def isSymmetric(self, root: TreeNode | None) -> bool:
        return self.isMirror(root.left, root.right)
        

"""
Notes

So a node.left should be equal to the node.right of the same level.
I brought the codes from Same Tree problem, and slightly modified it to compare left and right of
different nodes.
"""