import math
class MaxHeap:
    def heapify(self, numbers):
        last_parent_index =(len(numbers) // 2) - 1
        for i in range(last_parent_index, -1, -1):
            self.heapify_(numbers, i)
        return numbers

    def heapify_(self, array, index):
        larger_index = index

        left_index = index * 2 + 1
        if left_index < len(array) and  array[left_index] > array[larger_index]:
            larger_index = left_index

        right_index = index * 2 + 2
        if right_index < len(array) and  array[right_index] > array[larger_index]:
            larger_index = right_index

        if index == larger_index:
            return
        self.swap(array, index, larger_index)
        self.heapify_(array, larger_index)

    
    def swap(self, array, first, second):
        temp = array[first]
        array[first] = array[second]
        array[second] = temp

max_heap = MaxHeap()
list = [5, 3, 8, 4, 1, 2]
print(list)
print(max_heap.heapify(list))


