# Lookup O(1) 100, 104, 108 ... addresses in memory
# Insert (O(n) 10, 20, 30, 40, 50 ---> 10, 20, 30, 40, 50, _, _, _
# Delete (O(n) _, 20, 30, 40, 50) ---> Worst case since we need to shift to the left all items

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
        for i in range(index, self.size):
            if i + 1 < self.size:
                self.items[i] = self.items[i + 1]
            else:
                self.items[i] = None
        self.index -= 1
        
    def indexOf(self, item):
        for i in range(self.size):
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
myArray.max()

myArray2 = MyArray(3)
myArray2.insert(10)
myArray2.insert(40)
myArray2.insert(60)

myArray.intersect(myArray, myArray2)

myArray.reverse()