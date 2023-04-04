
class PriorityQueueArray():
    def __init__(self, size) -> None:
        self.size = size
        self.items = [None] * size
        self.count = 0

    def insert(self, data):
        if self.is_empty():
            self.items[self.count] = data
        else:
            if self.count == self.size:
                new_items = [None] * (self.size * 2)
                for i in range(0, self.size):
                    new_items[i] = self.items[i]
                self.size = self.size * 2
                self.items = new_items
            for i in range(self.count - 1, -1, -1):
                if data < self.items[i]:
                    self.items[i + 1] = self.items[i]
                    self.items[i] = data
                else:
                    self.items[i + 1] = data
                    break
        self.count += 1

    def is_empty(self):
        return self.count == 0
    
    def is_full(self):
        return self.size == self.count

    def print(self):
        for item in self.items:
            print(item, end=" - ")
        print("\n")

class PriorityQueue(PriorityQueueArray):
    def __init__(self, size) -> None:
        super().__init__(size)

queue = PriorityQueue(5)
queue.insert(3)
queue.insert(2)
queue.insert(5)
queue.insert(7)
queue.insert(1)
queue.insert(9)
queue.print()
