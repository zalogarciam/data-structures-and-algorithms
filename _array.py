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
        if (self.size > len(self.items)):
            self.items.append(item)
        else:
            print("Capacity is not enough, duplicating array size")
            self.size = self.size * 2
            self.items.append(item)
            for i in range(len(self.items), self.size):
                self.items.append(None)


    def removeAt(self, index):
        self.items.remove(self.items[index])

    def indexOf(self, item):
        for i in range(self.size):
            if self.items[i] == item:
                print(i)
                return i
        return -1

    def printItems(self):
        for i in range(self.size):
            print("Item "+ str(i) + ":" + str(self.items[i]))
        print(self.items)

myArray = MyArray(3)
myArray.insert(10)
myArray.insert(20)
myArray.insert(30)
myArray.insert(40)
myArray.indexOf(40)
myArray.printItems()