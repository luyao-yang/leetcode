# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = ListNode(0)
        first.next = head
        p1 = p2 = first

        while n:
            p2 = p2.next
            n = n - 1

        while p2.next is not None:
            p1 = p1.next
            p2 = p2.next

        p1.next = p1.next.next

        return first.next