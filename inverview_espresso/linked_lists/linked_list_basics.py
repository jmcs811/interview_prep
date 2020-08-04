
# linked list class
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

# creating a linked list
node = ListNode(1)
node.next = ListNode(2)
head = ListNode(0)
head.next = node

# 0 -> 1 -> 2

# traversing linked list
on = head
while (on != None):
    print(on.value)
    on = on.next