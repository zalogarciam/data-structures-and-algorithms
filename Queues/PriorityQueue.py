
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

    def enqueue(self, data):
        self.insert(data)

queue = PriorityQueue(5)
queue.enqueue(3)
queue.enqueue(2)
queue.enqueue(5)
queue.enqueue(7)
queue.enqueue(1)
queue.enqueue(9)
queue.enqueue(0)
queue.enqueue(4)
queue.enqueue(10)
queue.enqueue(6)
queue.print()
