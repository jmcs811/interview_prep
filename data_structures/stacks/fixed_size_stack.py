class FixedSizedStack:
    '''
    A stack implementation based on arrays
    Insert:     O(1) (size limit)
    Pop:        O(1)
    isEmpty:    O(1)
    stack_size: O(1)

    This stack implemention is fixed in size. In order to handle 
    growing and shrinking the underlying array, you would incur
    a O(n) cost when growing or shrinking.
    '''
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.list = [None] * self.capacity
        self.size = 0

    def push(self, item) -> None:
        '''
        Push item onto the array from left to right
        '''
        if self.size >= self.capacity:
            raise StackEmptyOrTooBigError
        
        self.list[self.size] = item
        self.size += 1

    def pop(self):
        '''
        pop the item from the end of the array
        '''
        if self.size <= 0:
            raise StackEmptyOrTooBigError
        item = self.list[self.size - 1]
        del self.list[self.size - 1]
        self.size -= 1
        return item

    def isEmpty(self):
        return self.size <= 0
    
    def stack_size(self) -> int:
        return self.size

    def __iter__(self):
        self.n = self.size
        return self

    def __next__(self):
        if self.n > 0:
            temp = self.list[self.n - 1]
            self.n -= 1
            return temp
        else:
            raise StopIteration

class StackEmptyOrTooBigError(Exception):
    pass

stack = FixedSizedStack(3)
stack.push(1)
stack.push(2)
stack.push(3)
for i in stack:
    print(i)
print(stack.stack_size())
#print(stack.push(4)) Throws StackEmptyOrTooBigError()
print(stack.pop())
print(stack.pop())
print(stack.pop())
#print(stack.pop()) Throws StackEmptyOrTooBigError()
print(stack.stack_size())
print(stack.isEmpty())
