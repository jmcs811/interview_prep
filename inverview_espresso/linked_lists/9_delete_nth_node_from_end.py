# leetcode 19

# def: remove the nth node from the end of a linked list
#      return the head

# i/o: head, nth node -> head

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

# TIME: O(n)
# SPACE: O(1)
def remove_nth_node_from_end(head, n):
    # count num of nodes O(n)
    on = head
    count = 1
    while on != None:
        count += 1
        on = on.next

    leftIndex = count - n - 1

    # handle head edge case
    if leftIndex == 0:
        return head.next

    # remove nth node O(n)
    on = head
    while leftIndex > 1: 
        leftIndex -= 1
        on = on.next
    
    on.next = on.next.next

    return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

remove_nth_node_from_end(head, 1)

on = head
count = 0
while on != None:
    count += 1
    print(on.value)
    on = on.next

print(count)