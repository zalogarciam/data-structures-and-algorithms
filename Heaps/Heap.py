import math
class Heap:
    def __init__(self) -> None:
        self.items = []
        self.size = 0

    def insert(self, value):
        self.items.append(value)        
        self.size += 1
        count = self.size
        index_parent = int((self.size/ 2) - 1)
        while (True):
            parent = self.items[index_parent]
            if parent < value:
                self.items[count - 1] = parent
                self.items[index_parent] = value
                index_parent = int(((index_parent + 1)/ 2) - 1)
                count = int(count / 2)
            else:
                break
        

    def remove(self):
        pass

    def print_heap(self):
        height = math.ceil((math.log(self.size + 1,2)))
        spaces = height
        for i in range(0, height):
            start = int(math.pow(2, i) - 1)
            end = int(math.pow(2, i + 1) - 2)
            for index, node in enumerate(self.items[start:end + 1]):
                print(spaces * "   " + str(node), end="")
            print()
            spaces = spaces - 1
        print(self.items)

heap = Heap()
heap.insert(15)
heap.insert(10)
heap.insert(3)
heap.insert(8)
heap.insert(12)
heap.insert(9)
heap.insert(4)
heap.insert(1)
heap.print_heap()