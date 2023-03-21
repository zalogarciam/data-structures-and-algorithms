class PointerArrayQueue():
    def __init__(self, size) -> None:
        self.size = size
        self.items = [None] * size
        self.index = 0
        self.front = 0
        self.back = 0

    def enqueue(self, data):
        if self.index == self.size:
            raise Exception("Queue is full")
        self.items[self.index] = data
        self.back += 1
        self.index += 1

    def dequeue(self):
        item = self.items[self.front]
        self.items[self.front] = None
        self.front += 1
        self.index -= 1
        return item

    def is_empty(self):
        return self.index == 0

    def is_full(self):
        return self.index == self.size

    def print_queue(self):
        for i in range(self.front, self.back):
            print(self.items[i])

queue = PointerArrayQueue(10)
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(10)
queue.enqueue(10)
queue.enqueue(10)
queue.enqueue(10)
queue.enqueue(10)
queue.dequeue()
queue.enqueue(10)
queue.print_queue()