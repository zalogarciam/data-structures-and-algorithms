class MinHeap:
    def heapify(self, numbers):
        last_parent_index =(len(numbers) // 2) - 1
        for i in range(last_parent_index, -1, -1):
            self.heapify_(numbers, i)
        return numbers

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

max_heap = MinHeap()
list = [5, 3, 8, 4, 1, 2]
print(list)
print(max_heap.heapify(list))