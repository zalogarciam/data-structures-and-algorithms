class MinHeap:
    def __init__(self, items) -> None:
        self.items = items

    def heapify(self):
        keys = [key for key in self.items]
        last_parent_index =(len(keys) // 2) - 1
        for i in range(last_parent_index, -1, -1):
            self.heapify_(keys, i)
        return keys

    def heapify_(self, array, index):
        min_index = index

        left_index = index * 2 + 1
        if left_index < len(array) and  array[left_index] < array[min_index]:
            min_index = left_index

        right_index = index * 2 + 2
        if right_index < len(array) and  array[right_index] < array[min_index]:
            min_index = right_index

        if index == min_index:
            return
        self.swap(array, index, min_index)
        self.heapify_(array, min_index)
        return array
    
    def swap(self, array, first, second):
        temp = array[first]
        array[first] = array[second]
        array[second] = temp

    def is_empty(self):
        return len(self.items) == 0

list = {5:"A", 3:"B", 8:"C", 4:"D", 1:"E", 2:"F"}
max_heap = MinHeap(list)
print(max_heap.heapify())
print(max_heap.is_empty())

class PriorityQueue:
    def __init__(self, dict) -> None:
        self.min_heap = MinHeap(dict)
        self.items = []

    def add(self, value, priority):
        pass

    def remove(self):
        pass

    def is_empty(self):
        return len(self.items) == 0

dict = {5:"A", 3:"B", 8:"C", 4:"D", 1:"E", 2:"F"}
queue = PriorityQueue(dict)

for key in list:
    queue.add(dict[key], key)

print(queue.is_empty())