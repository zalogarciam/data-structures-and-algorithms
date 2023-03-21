class PointerArrayQueue():
    def __init__(self, size) -> None:
        self.size = size
        self.items = [None] * size
        self.count = 0
        self.front = 0
        self.back = 0

    def enqueue(self, data):
        if self.count == self.size:
            raise Exception("Queue is full")
        self.items[self.back] = data
        self.back = (self.back + 1) % self.size
        self.count += 1

    def dequeue(self):
        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return item

    def peek(self):
        print("Front:" + str(self.front))
        return self.items[self.front]
    
    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def print_queue(self):
        for i in range(self.size):
            print(self.items[i], end=' -> ')

queue = PointerArrayQueue(5)
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(7)
queue.enqueue(10)
queue.dequeue()
queue.dequeue()
queue.enqueue(12)
queue.enqueue(14)
print(queue.peek())
queue.print_queue()