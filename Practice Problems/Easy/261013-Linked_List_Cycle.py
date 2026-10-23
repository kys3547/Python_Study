# LeetCode
# 141. Linked List Cycle

"""
Instruction

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
"""

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

# AI generated from here. A method to make and print linked list with a cycle

def build_list_with_cycle(values: list[int], pos: int) -> Optional[ListNode]:
    # Build a linked list from values. If pos != -1, link the tail back
    # to the node at index pos, which creates a cycle.
    if not values:
        return None

    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


solution = Solution()

test_cases = [
    ([3, 2, 0, -4], 1),
    ([1, 2], 0),
    ([1], -1),
]

for i, (values, pos) in enumerate(test_cases, start=1):
    head = build_list_with_cycle(values, pos)
    result = solution.hasCycle(head)
    print(f"Case {i} {values}, pos = {pos}:\t{result}")