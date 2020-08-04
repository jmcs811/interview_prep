# problem: implement and algorithm to find the kth to the last element

# Example
#   INPUT 1 -> 2 -> 3 -> 4 -> NONE, 2
#   OUTPUT 1 -> 2 -> 4 -> NONE

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def findKthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # get the count
        count = 1
        on = head
        while on != None:
            count += 1
            on = on.next
            
        one_before_removed = count - n

        if one_before_removed <= 0:
            return head.value
        
        if one_before_removed == 0:
            return head.next
        
        on = head
        while one_before_removed > 1:
            one_before_removed -= 1
            on = on.next
            
        return on.value

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

test = Solution()
print(test.findKthFromEnd(head, 4))