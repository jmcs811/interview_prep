class LinkedListQueue:
    '''
    Queue data structre based on linked lists. Items are
    added to the end of the list and are pulled from the 
    beginning of the list
    
    enqueue:    O(1)    adds to the queue
    dequeue:    O(1)    removes oldest from the queue
    isEmpty:    O(1)   
    stack_size: O(1)
    '''
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, item):
        '''
        add item to end of list
        '''
        if self.tail is None:
            self.head = ListNode(item)
            self.tail = self.head
        else:
            self.tail.next = ListNode(item)
            self.tail = self.tail.next
            self.tail.next = None
            self.size += 1

    def dequeue(self):
        '''
        remove item from beginning of list
        '''
        if self.head is None:
            raise StackEmpty
        item = self.head
        self.head = self.head.next
        self.size -= 1
        return item.val

    def isEmpty(self):
        return self.size <= 0

    def stack_size(self):
        return self.size

    def __iter__(self):
        self.n = self.head
        return self

    def __next__(self):
        if self.n is not None:
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

queue = LinkedListQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
for i in queue:
    print(i)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())