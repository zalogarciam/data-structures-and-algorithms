
class PriorityQueueArray():
    def __init__(self, size) -> None:
        self.size = size
        self.items = [None] * size
        self.count = 0

    def insert(self, data):
        pass

    def is_empty(self):
        return self.count == 0
    
    def is_full(self):
        return self.size == self.count

    def print(self):
        for item in self.items:
            print(item, end=" - ")


class PriorityQueue(PriorityQueueArray):
    def __init__(self, size) -> None:
        super().__init__(size)

queue = PriorityQueue(5)
queue.print()