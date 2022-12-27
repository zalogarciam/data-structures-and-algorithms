# Lookup O(1) 100, 104, 108 ... addresses in memory
# Insert (O(n) 10, 20, 30, 40, 50 ---> 10, 20, 30, 40, 50, _, _, _
# Delete (O(n) _, 20, 30, 40, 50) ---> Worst case since we need to shift to the left all items

numbers = [10, 20, 30];
print(numbers)

class MyArray():
    def __init__(self, size):
        self.size = size
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def removeAt(self, index):
        self.items.remove(self.items[index])

    def indexOf(self, item):
        for i in range(len(self.items)):
            if self.items[i] == item:
                return i

    def printItems(self):
        for i in range(len(self.items)):
            print(self.items[i])

myArray = MyArray(3)
myArray.insert(10)
myArray.insert(20)
myArray.insert(30)
myArray.insert(40)
myArray.indexOf(3)
myArray.printItems()