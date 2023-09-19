def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)): # i because first item is in the right position, therefore
            if array[j] < array[min_index]: # we can start from the next position and so on
                min_index = j
        swap(array, min_index, i)

def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

numbers = [7,3,1,4,6,2,3]
selection_sort(numbers)
print(numbers)

