#What is array list?
#An array list is a data structure that contains a collection of elements of the same type stored in
# contiguous memory locations. It also grows dynamically as the elements are added to it.


class FixedSizeArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def __getitem__(self):
        return repr(self.array[:self.size])
    def __push__(self, value):
        if self.size == self.capacity:
            self.capacity *= 2
            new_array = [None] * self.capacity
            for i in range(self.size):
                new_array[i] = self.array[i]
            self.array = new_array
        self.array[self.size] = value
        self.size += 1
        print(self.array)
    def __pop__(self):
        if self.size == 0:
            return None
        self.size -= 1
        print('array',self.array)
        return self.array[self.size]
 

fixedSizeArray = FixedSizeArray(5)
fixedSizeArray.__push__(2)
fixedSizeArray.__push__(2)
fixedSizeArray.__push__(3)
fixedSizeArray.__push__(3)
fixedSizeArray.__push__(4)
fixedSizeArray.__push__(5)
fixedSizeArray.__push__(5)
fixedSizeArray.__push__(5)
fixedSizeArray.__push__(5)
fixedSizeArray.__push__(5)
fixedSizeArray.__push__(5)
fixedSizeArray.__push__(5)
fixedSizeArray.__push__(10)
print(fixedSizeArray.__pop__())
print(fixedSizeArray.__getitem__())