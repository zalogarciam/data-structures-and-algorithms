class MyArray():
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.index = 0

    def insert(self, item):
        if (self.size == self.index):
            newItems = [None] * self.size * 2
            for i in range(self.size):
                newItems[i] = self.items[i]
            self.items = newItems
            self.size = self.size * 2
        
        self.items[self.index] = item
        self.index += 1

    def removeAt(self, index):
        if index < 0 or index > self.size - 1:
            raise Exception("Index out of range")
        else:
            removed_item = self.items[index]
            for i in range(index, self.size):
                if i + 1 < self.size:
                    self.items[i] = self.items[i + 1]
                else:
                    self.items[i] = None
            self.index -= 1
            return removed_item

    def indexOf(self, item):
        for i in range(self.index):
            if self.items[i] == item:
                print(i)
                return i
        return -1

    def getItem(self, index):
        return self.items[index]

    def printItems(self):
        for i in range(self.index):
            if (self.items[i] != None):
                print("Item "+ str(i) + ": " + str(self.items[i]))

    def max(self):
        max = -1
        for i in range(self.index):
            if self.items[i] > max:
                max = self.items[i]
        print("Max: " + str(max))
        return max

    def intersect(self, first_array, second_array):
        dict = {}
        for i in range(first_array.index):
            if first_array.getItem(i) not in dict:
                dict[first_array.getItem(i)] = 1
            else:
                dict[first_array.getItem(i)] += 1

        for i in range(second_array.index):
            if second_array.getItem(i) not in dict:
                dict[second_array.getItem(i)] = 1
            else:
                dict[second_array.getItem(i)] += 1
        
        for key in dict:
            if (dict[key] > 1):
                print("Intersecting: " + str(key))

    def reverse(self):
        for i in range(self.index - 1, - 1, - 1):
            print("Item "+ str(i) + ": " + str(self.items[i]))

    def insertAt(self, item, index):
        for i in range(self.index, index , -1):
            self.items[i] = self.items[i - 1]
        self.items[index] = item

class ArrayStack(MyArray):
    def __init__(self, size):
        super().__init__(size)

    def push(self, value):
        self.insert(value)

    def pop(self):
        return self.removeAt(self.index - 1)

    def peek(self):
        return self.items[self.index - 1]

    def is_empty(self):
        return self.index == 0

    def print_stack(self):
        self.printItems()

class ArrayQueue(MyArray):
    def __init__(self, size):
        super().__init__(size)

    def add(self, value):
        self.insert(value)

    def remove(self):
        return self.removeAt(0)

    def peek(self):
        return self.items[self.index - 1]

    def is_empty(self):
        return self.index == 0

    def print_queue(self):
        self.printItems()

    def reverse_queue(self):
        reversed_queue = []
        for i in range(len(self.items) - 1, -1, -1):
            if (self.items[i] is not None):
                reversed_queue.append(self.items[i])
        return reversed_queue
    
    def reverse_queue_2(self, size):
        stack = ArrayStack(size)
        for i in range(0, size - 1):
            if self.items[i] != None:
                stack.insert(self.items[i])
        while stack.is_empty() == False:
            item = stack.pop()
            if item is not None:
                print(item, end='-')

 

queue = ArrayQueue(10)
queue.add(2)
queue.add(4)
queue.add(5)
queue.remove()
queue.add(1)
queue.peek()
queue.is_empty()
# queue.print_queue()
# print(queue.reverse_queue())
print(queue.reverse_queue_2(10))