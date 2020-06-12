# Task 1: Implement a ring buffer data structure

'''
Our ring buffer is a non-groable buffer with a fixed size. When it fills up, 
adding another element overwrites the oldest one that was still being kept.

Example:

buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']
'''


class RingBuffer:
    # class that implements a not-yet FULL buffer
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity
        

    def append(self, item):
        # add item to storage list
        '''
        the append method adds the given element to the buffer, which will
        overwrite the oldest one.
        '''
        self.storage[self.current] = item
        # length of list
        # if self.current >= len(self.storage) - 1:
        if self.current < (self.capacity - 1):
            self.current += 1
        else: 
            self.current = 0

    def get(self):
        '''
        Return a list of elements from the oldest to the newest.
        '''
        # Our list:
        list = [item for item in self.storage if item]
        return list