import math
class MinHeap:
    def __init__(self) -> None:
        self.items = []
        self.size = 0

    def insert_(self, value):
        self.items.append(value)
        self.size += 1
        self.bubble_up()
        
    def bubble_up(self):
        index = self.size - 1
        while index > 0 and self.items[index] < self.items[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)
    
    def parent(self, index):
        return (index - 1)//2

    def swap(self, first, second):
        temp = self.items[first]
        self.items[first] = self.items[second]
        self.items[second] = temp

    def remove_(self):
        root = self.items[0]
        if self.size == 0: raise Exception("Empty heap")
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.size -= 1
        self.bubble_down()       
        return root

    def bubble_down(self):
        index = 0
        while index <= self.size and not self.is_valid_parent(index):
            min_child_index = self.min_child_index(index)
            self.swap(index, min_child_index)
            index = min_child_index

    def min_child_index(self, index):
        if not self.has_left_child(index):
            return index
        if not self.has_right_child(index):
            return self.left_child_index(index)
        left  = self.left_child(index)
        right = self.right_child(index)
        if left <= right:
             return self.left_child_index(index)
        else:
             return self.right_child_index(index)

    def has_left_child(self, index):
        return self.left_child_index(index) < self.size
    
    def has_right_child(self, index):
        return self.right_child_index(index) < self.size

    def is_valid_parent(self, index):
        if not self.has_left_child(index):
            return True
        
        is_valid = self.items[index] <= self.left_child(index)

        if self.has_right_child(index):
            is_valid = is_valid and self.items[index] <= self.right_child(index)
        return is_valid

    def left_child(self, index):
        return self.items[self.left_child_index(index)]
    
    def right_child(self, index):
        return self.items[self.right_child_index(index)]

    def left_child_index(self, index):
        return index * 2 +  1
    
    def right_child_index(self, index):
        return index * 2 +  2
        
    def is_empty(self):
        return self.size == 0

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
        print(self.items)

min_heap =MinHeap()
min_heap.insert_(5)
min_heap.insert_(3)
min_heap.insert_(8)
min_heap.insert_(4)
min_heap.insert_(1)
min_heap.insert_(2)
# min_heap.print_heap()

class PriorityQueue:
    def __init__(self) -> None:
        self.min_heap = MinHeap()
        self.items = {}

    def add(self, value, priority):
        self.items[priority] = value
        self.min_heap.insert_(priority)

    def remove(self):
        pop = self.min_heap.remove_()
        self.items.pop(pop)
        return pop

    def is_empty(self):
        return len(self.items) == 0
    
    def print_priority(self):
        self.min_heap.print_heap()
        for item in self.items:
            print('Key: ', item, 'Value: ', self.items[item])

queue = PriorityQueue()
queue.add("A", 5)
queue.add("B", 3)
queue.add("C", 8)
queue.add("D", 4)
queue.add("E", 1)
queue.add("F", 2)
queue.print_priority()
queue.remove()
queue.print_priority()
queue.remove()
queue.print_priority()

# for key in list:
#     queue.add(dict[key], key)

# print(queue.is_empty())