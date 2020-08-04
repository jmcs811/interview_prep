# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # count number of nodes
        on = head
        count = 0
        while on != None:
            count += 1
            on = on.next
            
        middle = int((0+count) / 2) - 1
        
        on = head
        while middle >= 0:
            middle -= 1
            on = on.next
            
        print(on.val)
        return on
        