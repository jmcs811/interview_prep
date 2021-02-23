import random
class RandomQueue:
    '''
    A random queue is similar to a normal queue, but
    the items are removed at random.
    '''
    def __init__(self):
        self.size = 0
        self.items = [None] * 4

    def enqueue(self, item):
        if item is None:
            raise NoneError
        self.items[self.size] = item
        self.size += 1
        if len(self.items) == self.size:
            self.items = self._resize(self.items, len(self.items) * 2)

    def dequeue(self):
        if self.size == 0:
            raise QueueEmptyError

        r = int(random.uniform(0, self.size - 1))
        res = self.items[r]
        if r != self.size - 1:
            self.items[r] = self.items[self.size - 1]
        self.items[self.size - 1] = None
        self.size -= 1
        if self.size > 0 and self.size <= int(len(self.items) / 4):
            self.items = self._resize(self.items, len(self.items) / 2)
        return res

    def _resize(self, items, capacity):
        temp = [None] * int(capacity)
        for i in range(min(len(temp), len(items))):
            temp[i] = items[i]
        return temp

    def sample(self):
        r = int(random.uniform(0, self.size - 1))
        return self.items[r]

    def queue_size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.size:
            temp = self.sample()
            self.n += 1
            return temp
        else:
            raise StopIteration

class NoneError(Exception):
    pass

class QueueEmptyError(Exception):
    pass

queue = RandomQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(5)
queue.enqueue(5)
queue.enqueue(5)
print(queue.dequeue())
print(queue.sample())
print(queue.sample())
print("ITERATION\n\n")
for i in queue:
    print(i)