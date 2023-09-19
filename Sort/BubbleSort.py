def bubble_sort(array):
    is_sorted = True
    for i in range(len(array)):
        is_sorted = True
        for j in range(1, len(array) - i): # -i because every iteration the last element 
            if array[j] < array[j-1]: #is in the correct position, hence, not necessary to iterate it
                swap(array,j , j-1)
                is_sorted = False
        if is_sorted: return # if in the first iteration it is all ordered, we dont need to sort it

def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

numbers = [7,3,1,4,6,2,3]
sort = bubble_sort(numbers)
print(numbers)