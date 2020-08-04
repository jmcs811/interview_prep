# Given a singly linked list, determine if it is a palindrome.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ht = []
        
        on = head
        while on != None:
            ht.append(on.val)
            on = on.next
            
        left = 0
        right = len(ht) - 1
        
        while (left < right):
            if ht[left] != ht[right]:
                return False
            left += 1
            right -= 1
            
        return True