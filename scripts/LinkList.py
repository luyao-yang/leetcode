class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#create a linklist
a = [1,2,4]
head = l =ListNode(0)
for value in a:
    head.next = ListNode(value)
    head = head.next

#traverse a linklist
