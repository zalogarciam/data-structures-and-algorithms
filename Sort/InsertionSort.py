#               Best        Worst
# Iteration     O(n)        O(n)
# Shift Item    O(1)        O(n) # 1 if the array is sorted in asc
# Total         O(n)        O(n^2)

def insertion_sort(array):
    for i in range(1, len(array)):
        current = array[i] # store element 
        j = i - 1
        while j >= 0 and array[j] > current:
            array[j+1] = array[j] # shift elements to the right
            j-= 1
        array[j+1] = current

numbers = [7,3,1,4,6,2,3]
sort = insertion_sort(numbers)
print(numbers)