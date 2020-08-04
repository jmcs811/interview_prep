# problem: write code to remove duplicates from an unsorted linked list.

# intial idea
# create a set
# loop through the list
# if value in set, remove it
# add val to set

class Node:
    def __init__(self):
        self.value = None
        self.next = None

def remove_dupes(head):
    hs = set()
    on = head
    prev = None
    while on != None:
        if on.value in hs:
            # remove
            prev.next = on.next
        else:
            hs.add(on.value)
            prev = on
        
        on = on.next


