class Bag:
    '''
    The bag data stuct represents a collection of items.
    Items can only be added to the bag and they can be
    iterated over. Think of it as a bag of marbles

    add: O(1)
    '''
    def __init__(self):
        self.size = 0
        self.head = None

    def add(self, item):
        temp = self.head
        self.head = ListNode(item)
        self.head.next = temp
        self.size += 1

    def isEmpty(self):
        return self.size <= 0

    def bag_size(self):
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

bag = Bag()
bag.add(5)
bag.add(3)
bag.add(2)
for i in bag:
    print(i)
print(bag.isEmpty())
print(bag.bag_size())