import math
class Heap:
    def __init__(self) -> None:
        self.items = []
        self.size = 0

    def insert(self, value):
        self.items.append(value)        
        self.size += 1
        count = self.size
        index_parent = int((self.size/ 2) - 1)
        # Bubble up
        while self.items[index_parent] < value:
            parent = self.items[index_parent]
            self.items[count - 1] = parent
            self.items[index_parent] = value
            index_parent = int(((index_parent + 1)/ 2) - 1)
            count = int(count / 2)

    def insert_(self, value):
        self.items.append(value)
        self.size += 1
        self.bubble_up()
        
    def bubble_up(self):
        index = self.size - 1
        while index > 0 and self.items[index] > self.items[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)
    
    def parent(self, index):
        return math.ceil((index - 1)/2)

    def swap(self, first, second):
        temp = self.items[first]
        self.items[first] = self.items[second]
        self.items[second] = temp

    def remove_(self):
        root = self.items[0]
        if self.size == 0: raise Exception("Empty heap")
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.bubble_down()       
        self.size -= 1
        return root

    def bubble_down(self):
        index = 0
        while index <= self.size and not self.is_valid_parent(index):
            larger_child_index = self.larger_child_index(index)
            self.swap(index, larger_child_index)
            index = self.larger_child_index(index)

    def larger_child_index(self, index):
        if not self.has_left_child(index):
            return index
        if not self.has_right_child(index):
            return self.left_child_index(index)
        return self.left_child_index(index) if self.left_child(index) > self.right_child(index) else self.right_child_index(index) 

    def has_left_child(self, index):
        return self.left_child_index(index) <= self.size
    
    def has_right_child(self, index):
        return self.right_child_index(index) <= self.size

    def is_valid_parent(self, index):
        if not self.has_left_child(index):
            return True
        
        is_valid = self.items[index] >= self.left_child(index)

        if not self.has_right_child(index):
            is_valid = is_valid and self.items[index] >= self.right_child(index)
        return is_valid

    def left_child(self, index):
        return self.items[self.left_child_index(index)]
    
    def right_child(self, index):
        return self.items[self.right_child_index(index)]

    def left_child_index(self, index):
        return index * 2 +  1
    
    def right_child_index(self, index):
        return index * 2 +  2

    def remove(self):
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.size -= 1
        count = 0
        child_index = (self.items.index(self.items[count]) * 2) + 1
        # Bubble down
        while self.items[count] < self.items[child_index]:
            child = self.items[child_index]
            current = self.items[count]
            self.items[count] = child
            self.items[child_index] = current
            child_index = (child_index * 2) + 1
            count = (count * 2) + 1
            
    def print_heap(self):
        height = math.ceil((math.log(self.size + 1,2)))
        spaces = height
        for i in range(0, height):
            start = int(math.pow(2, i) - 1)
            end = int(math.pow(2, i + 1) - 2)
            for index, node in enumerate(self.items[start:end + 1]):
                print(spaces * "   " + str(node), end="")
            print()
            spaces = spaces - 1
        print(self.items)

heap = Heap()
heap.insert_(15)
heap.insert_(10)
heap.insert_(3)
heap.insert_(8)
heap.insert_(12)
heap.insert_(9)
heap.insert_(4)
heap.insert_(1)
heap.insert_(24)
heap.print_heap()
heap.remove_()
heap.print_heap()

