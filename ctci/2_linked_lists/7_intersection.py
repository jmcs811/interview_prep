# Write a program to find the node at which the intersection of two singly linked lists begins.

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
        TIME: O(n)
        SPACE: O(n)
        '''
        hs = set()
        
        on = headA
        while on != None:
            hs.add(on)
            on = on.next
            
        
        on = headB
        while on != None:
            if on in hs:
                return on
            on = on.next
            
        return None

    
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
        TIME: O(n)
        SPACE: O(1)
        '''
        lenA = 0
        lenB = 0
        
        on = headA
        while on != None:
            lenA += 1
            on = on.next
            
        on = headB
        while on != None:
            lenB += 1
            on = on.next
            
        
        if (lenA > lenB):
            diff = lenA - lenB
            while diff:
                headA = headA.next
                diff -= 1
            
        else:
            diff = lenB - lenA
            while diff:
                headB = headB.next
                diff -= 1
                
        
        while headA and headB:
            if (headA == headB):
                return headA
            headA = headA.next
            headB = headB.next
            
        return None