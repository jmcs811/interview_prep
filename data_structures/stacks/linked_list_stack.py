class LinkListStack:
    '''
    A stack implementation based on linked lists
    Insert:     O(1) (no size limit)
    Pop:        O(1)
    isEmpty:    O(1)
    stack_size: O(1)
    '''
    def __init__(self):
        self.size = 0
        self.head = None

    def push(self, item):
        # insert at the head of the list
        old_first = self.head
        self.head = ListNode(item)
        self.head.next = old_first
        self.size += 1

    def pop(self):
        if self.head is None:
            raise StackEmpty
        item = self.head
        self.head = self.head.next
        self.size -= 1
        return item.val

    def isEmpty(self):
        return self.head == None

    def stack_size(self):
        return self.size

    def __iter__(self):
        self.n = self.head
        return self

    def __next__(self):
        if self.n != None:
            temp = self.n
            self.n = self.n.next
            return temp.val
        else:
            raise StopIteration

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class StackEmpty(Exception):
    pass

stack = LinkListStack()
stack.push(1)
stack.push(2)
stack.push(3)
for i in stack:
    print(i)
print(stack.pop())
print(stack.stack_size())
stack.pop()
stack.pop()
print(stack.stack_size())
stack.push(5)
stack.pop()
print(stack.stack_size())