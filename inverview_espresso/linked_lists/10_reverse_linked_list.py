
# TIME: O(n)
# SPACE: O(1)
def reverseListIterative(head):
    on = head
    prev = None

    while (on != None):
        temp = on.next
        on.next = prev
        prev = on
        on = temp

    return prev

# TIME: O(n)
# SPACE: O(n) or O(1)
def reverseListRecursive(on, prev=None):
    if on is None:
        return prev
    temp = on.next
    on.next = prev
    return reverseListRecursive(prev, temp)
