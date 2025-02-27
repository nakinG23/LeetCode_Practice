class DynamicArray:
    
    def __init__(self, capacity: int):
        # Initialize empty array with given capacity
        self.capacity = capacity
        self.size = 0
        # Create a list with initial capacity
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        # Return element at index i
        return self.arr[i]

    def set(self, i: int, n: int) -> Null:
        # Set element at index i to value n
        self.arr[i] = n

    def pushback(self, n: int) -> Null:
        # If array is full, resize first
        if self.size == self.capacity:
            self.resize()
        # Add new element at the end
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # Remove and return the last element
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> Null:
        # Double the capacity
        self.capacity *= 2
        # Create new array with doubled capacity
        new_arr = [0] * self.capacity
        # Copy elements from old array to new array
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        # Return current number of elements
        return self.size
    
    def getCapacity(self) -> int:
        # Return current capacity
        return self.capacity
    
