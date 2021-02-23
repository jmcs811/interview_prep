class Deque:
    '''
    This is a double ended queue, it supports removing from
    the front and the back of the list
    '''
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def add_first(self, item):
        if item is None:
            raise NoneError
        node = ListNode(item)
        node.next = self.head
        node.prev = None
        if self.size == 0:
            self.head = node
            self.tail = self.head
        else:
            self.head.prev = node
            self.head = node
        self.size += 1
        

    def add_last(self, item):
        if item is None:
            raise NoneError
        node = ListNode(item)
        node.next = None
        node.prev = self.tail
        if self.size == 0:
            self.tail = node
            self.head = self.tail
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def remove_first(self):
        if self.size <= 0:
            raise DequeEmpty
        temp = self.head
        self.head = self.head.next
        if self.size == 1:
            self.tail = None
        else:
            self.head.prev = None
        self.size -= 1
        return temp.val

    def remove_last(self):
        if self.size <= 0:
            raise DequeEmpty
        temp = self.tail
        self.tail = self.tail.prev
        if self.size == 1:
            self.head == None
        else:
            self.tail.next = None
        self.size -= 1
        return temp.val
    
    def deque_size(self):
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
        self.prev = None

class NoneError(Exception):
    pass

class DequeEmpty(Exception):
    pass


deque = Deque()
deque.add_first(3)
deque.add_first(2)
deque.add_first(1)
deque.add_last(4)
print(deque.remove_first()) # 1
print(deque.remove_first()) # 2
print(deque.remove_last())  # 4
print(deque.remove_last())  # 3
#print(deque.remove_last())  # DequeEmpty error
deque.add_first(2)
deque.add_last(3)
deque.add_first(1)
deque.add_last(4)
for i in deque:
    print(i)

