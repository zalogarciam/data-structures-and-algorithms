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
        deleted = None
        if index < 0 or index > self.size - 1:
            raise Exception("Index out of range")
        else:
            for i in range(index, self.size):
                if i + 1 < self.size:
                    if self.items[i] != None:
                        deleted = self.items[i]
                        self.items[i] = self.items[i + 1]
                else:
                    self.items[i] = None
            self.index -= 1
        return deleted

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

stack = ArrayStack(4)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.pop())
print(stack.peek())
print(stack.is_empty())
stack.print_stack()
