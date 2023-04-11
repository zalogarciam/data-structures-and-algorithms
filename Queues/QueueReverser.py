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
        print("[", end="")
        for i in range(self.index):
            if (self.items[i] != None):
                print(str(self.items[i]), end=", ")
        print("]", end="")

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

    def reverse(self, k):
        pass

queue = ArrayQueue(5)
queue.add(10)
queue.add(20)
queue.add(30)
queue.add(40)
queue.add(50)
queue.print_queue()

