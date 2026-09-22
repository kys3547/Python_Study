# LeetCode
# 21. Merge Two Sorted Lists

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

"""
# Linked List Practices

# Creating & Printing Linked Lists
a = ListNode("a")
b = ListNode("b")
c = ListNode("c")

a.next = b
b.next = c

current = a
while current:
    print(current.val)
    current = current.next

print()

# Getting the length of a given linked list
def get_length(head: ListNode) -> int:
    count = 0
    current = head

    while current:
        count += 1
        current = current.next

    return count

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print(get_length(head))

print()

# Searching if a linked list has a certain value
def contains(head: ListNode, target: int) -> bool:
    current = head

    while current:
        if current.val == target:
            return True
        current = current.next

    return False

head = ListNode(5, ListNode(3, ListNode(9)))
print(contains(head, 3))
print(contains(head, 7))

print()

# Finding the last node of a linked list
def find_last(head: ListNode) -> ListNode:
    current = head

    while current.next:
        current = current.next

    return current

head = ListNode(1, ListNode(2, ListNode(3)))
last = find_last(head)
print(last.val)
print(last.next)

print()

# Reversing a linked list
def reverse(head: ListNode) -> ListNode:
    current = head
    prev = None
    oldNext = None

    while current:
        oldNext = current.next
        current.next = prev
        prev = current
        current = oldNext

    return prev
"""

# function to convert a linked list into a list for printing
def linked_lst_to_lst(head: ListNode) -> list:
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result


# Merging Two Sorted Lists
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        current1 = list1
        current2 = list2
        dummy = ListNode()
        tail = dummy

        while current1 and current2:
            if current1.val < current2.val:
                tail.next = current1
                tail = tail.next
                current1 = current1.next
            else:
                tail.next = current2
                tail = tail.next
                current2 = current2.next

        tail.next = current1 if current1 else current2
        
        return dummy.next

solution = Solution()

print("Case 1 [1, 2, 4], [1, 3, 4]:\t", linked_lst_to_lst(solution.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4))))))
print("Case 2 [], []:\t\t\t", linked_lst_to_lst(solution.mergeTwoLists(ListNode(), ListNode())))
print("Case 3 [], [0]:\t\t\t", linked_lst_to_lst(solution.mergeTwoLists(ListNode(), ListNode(0))))