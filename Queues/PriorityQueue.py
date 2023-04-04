
class PriorityQueueArray():
    def __init__(self, size) -> None:
        self.size = size
        self.items = [None] * size
    def print(self):
        for item in self.items:
            print(item, end=" - ")


class PriorityQueue(PriorityQueueArray):
    def __init__(self, size) -> None:
        super().__init__(size)

queue = PriorityQueue(5)
queue.print()