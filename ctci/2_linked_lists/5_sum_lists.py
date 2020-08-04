# problem: you have two numbers represented by linked lists, where each node
#   contains a single digit. The digits are stored in revers order such that
#   the 1''s digit is at the haed of the list. Write a function that adds \
#   two numbers and retuns the sum as a linked list
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        answer = ListNode(0)
        
        carry_bit = 0
        
        on1 = l1
        on2 = l2
        on3 = answer
        carry_bit = 0
        while on1 != None and on2 != None:
            temp_sum = on1.val + on2.val + carry_bit
            carry_bit = 0
            if temp_sum >= 10:
                temp_sum = temp_sum % 10
                carry_bit = 1
            
            on3.next = ListNode(temp_sum)
            on3 = on3.next
            on1 = on1.next
            on2 = on2.next
            
        while on1 != None:
            temp_sum = on1.val + carry_bit
            carry_bit = 0
            if temp_sum >= 10:
                temp_sum = temp_sum % 10
                carry_bit = 1
            on3.next = ListNode(temp_sum)
            on3 = on3.next
            on1 = on1.next
            
        while on2 != None:
            temp_sum = on2.val + carry_bit
            carry_bit = 0
            if temp_sum >= 10:
                temp_sum = temp_sum % 10
                carry_bit = 1
            on3.next = ListNode(temp_sum)
            on3 = on3.next
            on2 = on2.next
            
        if carry_bit == 1 and on1 == None and on2 == None:
            on3.next = ListNode(1)
            on3 = on3.next
        
        return answer.next
        

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

head1 = ListNode(2)
head1.next = ListNode(3)
head1.next.next = ListNode(4)

test = Solution()
temp = test.addTwoNumbers(head, head1)

while temp != None:
    print(temp.val)
    temp = temp.next