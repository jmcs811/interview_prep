class Solution:
    '''
    TIME: O(n)
    SPACE: O(n)
    '''
    def hasCycle(self, head: ListNode) -> bool:
        hs = set()
        on = head
        while on != None:
            if on in hs:
                return True
            hs.add(on)
            on = on.next
        return False

    def hasCycleConstantMemory(self, head):
        '''
        TIME: O(n)
        SPACE: O(1)
        '''
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
            
        return False
            