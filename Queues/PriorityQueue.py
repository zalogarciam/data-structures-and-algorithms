
class PriorityQueueArray():
    def __init__(self, size) -> None:
        self.size = size
        self.items = [None] * size
        self.count = 0

    def insert(self, data):
        pos = 0

        if self.count == self.size:
            new_items = [None] * (self.size * 2)
            for i in range(0, self.size):
                new_items[i] = self.items[i]
            self.size = self.size * 2
            self.items = new_items

        for i in range(self.count - 1, -1, -1):
            pos = i
            if data < self.items[i]:
                self.items[i + 1] = self.items[i]
            else:
                pos = pos + 1
                break
            
        self.items[pos] = data
        self.count += 1

    def remove(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        self.items[self.count - 1] = None
        self.count -= 1

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

    def dequeue(self):
        self.remove()

queue = PriorityQueue(5)
queue.enqueue(3)
queue.print()
queue.enqueue(2)
queue.print()
queue.enqueue(5)
queue.print()
queue.enqueue(7)
queue.print()
queue.enqueue(1)
# queue.dequeue()
queue.print()
queue.enqueue(9)
queue.print()
queue.enqueue(0)
queue.print()
queue.enqueue(4)
queue.print()
queue.enqueue(10)
queue.print()

queue.enqueue(6)
# queue.dequeue()
queue.print()
