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


class StackWithTwoQueues():
    def __init__(self, size):
        self.q1 = ArrayQueue(size)
        self.q2 = ArrayQueue(size)
        self.count = 0

    def push(self, data):
        if self.q1.is_empty():
            self.q1.add(data)
        else:
            for i in range (self.q1.index):
                self.q2.add(self.q1.remove())
            self.q1.add(data)

            for i in range(self.q2.index):
                self.q1.add(self.q2.remove())
        self.count +=1
  

    def pop(self):
        self.count -= 1
        return self.q1.remove()

    def peek(self):
        return self.q1.peek()

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def print(self):
        print("Q1")
        self.q1.print_queue()
        print("\n\nQ2")
        self.q2.print_queue()


stack = StackWithTwoQueues(5)
stack.push(3)
stack.push(4)
stack.push(1)
stack.push(5)
stack.push(7)
print(stack.pop())
stack.print()

