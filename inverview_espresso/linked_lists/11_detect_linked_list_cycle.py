class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

# TIME: O(n)
# SPACE: O(n)
def hasCycle(head):
    nodes = set()

    on = head
    while on != None:
        if on in nodes:
            return True

        nodes.add(on)
        on = on.next

    return False

# TIME: O(n)
# SPACE: (1)
def hasCycleFloyds(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
        
    return False



