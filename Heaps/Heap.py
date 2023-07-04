import math
class Heap:
    def __init__(self) -> None:
        self.items = []
        self.size = 0

    def insert(self, value):
        self.items.append(value)        

        self.size += 1

    def remove(self):
        pass

    def print_heap(self):
        height = math.ceil((math.log(self.size + 1,2)))
        spaces = height
        for i in range(0, height):
            start = int(math.pow(2, i) - 1)
            end = int(math.pow(2, i + 1) - 2)
            for node in self.items[start:end + 1]:
                print(spaces * "   " + str(node), end="")
            print()
            spaces = spaces - 1
        

heap = Heap()
heap.insert(15)
heap.insert(10)
heap.insert(3)

heap.print_heap()