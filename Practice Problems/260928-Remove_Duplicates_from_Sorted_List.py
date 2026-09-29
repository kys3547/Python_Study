# LeetCode
# 83. Remove Duplicates from Sorted List

"""
Instruction

Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.
"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        current = head

        while current:
            if current.next != None and current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


"""
Note

Iterate through all elements, store the previous element in a variable, compare it
(after trying it)
Okay, so it is very difficult to access to the previous node without adding self.prev to ListNode class.
I should try comparing current node with the next node.
If current.val and current.next.val are same,
current.next = current.next.next (so that the linked list skips the next node).
If not, move current to the next node.

I added current.next != None to prevent runtime error.
(Without this, the while loop might try to call current.next when it's None)

At the end, return head.

Ahh... Linked list makes me feel headache. But beautifully done!
"""