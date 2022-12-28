# Lookup O(1) 100, 104, 108 ... addresses in memory
# Insert (O(n) 10, 20, 30, 40, 50 ---> 10, 20, 30, 40, 50, _, _, _
# Delete (O(n) _, 20, 30, 40, 50) ---> Worst case since we need to shift to the left all items

class MyArray():
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.index = 0

    def insert(self, item):
        if (self.size > self.index):
            self.items[self.index] = item
        else:
            print("Capacity is not enough, duplicating array size")
            newItems = [None] * self.size * 2
            for i in range(self.size):
                newItems[i] = self.items[i]
            self.items = newItems
            self.size = self.size * 2
            self.items[self.index] = item

        self.index += 1

    def removeAt(self, index):
        for i in range(index, self.size):
            if i + 1 < self.size:
                self.items[i] = self.items[i + 1]
            else:
                self.items[i] = None
        
    def indexOf(self, item):
        for i in range(self.size):
            if self.items[i] == item:
                print(i)
                return i
        return -1

    def printItems(self):
        for i in range(self.size):
            print("Item "+ str(i) + ": " + str(self.items[i]))
        print(self.items)

myArray = MyArray(3)
myArray.insert(10)
myArray.insert(20)
myArray.insert(30)
myArray.insert(40)
myArray.insert(50)
myArray.insert(60)
myArray.printItems()
myArray.removeAt(3)
myArray.indexOf(40)
myArray.printItems()