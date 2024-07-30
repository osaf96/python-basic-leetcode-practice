# What is array buffer?
# An array buffer is a data structure that contains a collection of 
# elements of the same type stored in
# contiguous memory locations. It also grows dynamically as the elements are added to it.


#implementation of array buffer In python
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum number of elements
        self.buffer = [None] * capacity  # Initialize buffer with None values
        self.head = 0  # Points to the position to read from
        self.tail = 0  # Points to the position to write to
        self.size = 0  # Current number of elements in the buffer

    def push(self, value):
        if self.size == self.capacity:
            # Buffer is full, overwrite the oldest data
            self.head = (self.head + 1) % self.capacity
        else:
            self.size += 1
        
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity

    def pop(self):
        if self.size == 0:
            raise IndexError("Pop from an empty buffer")
        
        value = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return value

    def __repr__(self):
        if self.size == 0:
            return "RingBuffer([])"
        
        if self.tail >= self.head:
            return f"RingBuffer({self.buffer[self.head:self.tail]})"
        else:
            return f"RingBuffer({self.buffer[self.head:] + self.buffer[:self.tail]})"

# Example usage
rb = RingBuffer(5)

# Push elements into the buffer
rb.push(1)
rb.push(2)
rb.push(3)
print(rb)  # Output: RingBuffer([1, 2, 3])

# Pop an element from the buffer
print(rb.pop())  # Output: 1
print(rb)  # Output: RingBuffer([2, 3])

# Add more elements
rb.push(4)
rb.push(5)
rb.push(6)  # This will overwrite the oldest element (2)
print(rb)  # Output: RingBuffer([3, 4, 5, 6])

# Pop all elements
print(rb.pop())  # Output: 3
print(rb.pop())  # Output: 4
print(rb.pop())  # Output: 5
print(rb.pop())  # Output: 6
