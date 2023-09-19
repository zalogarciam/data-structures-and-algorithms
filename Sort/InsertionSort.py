def insertion_sort(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and array[j] > current:
            array[j+1] = array[j]
            j-= 1
        array[j+1] = current

numbers = [7,3,1,4,6,2,3]
sort = insertion_sort(numbers)
print(numbers)