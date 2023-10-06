#               Best        Worst
# Partioning    O(n)        O(n)
# # of times    O(log n)    O(n)    depends on the pivot
# Total         O(n log(n)) O(n^2)
# Space         O(log(n))   O(n)

def quick_sort(array, start, end):
    if start >= end: return
    
    boundary = partition(array, start, end)
    quick_sort(array, start, boundary - 1)
    quick_sort(array, boundary + 1, end)

def partition(array, start, end):
    pivot = array[end]
    boundary = start - 1
    for i in range(start, end + 1):
        if array[i] <= pivot:
            boundary += 1
            swap(array, i, boundary)
    return boundary

def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

numbers = [15,6,3,1,22,10,13]
quick_sort(numbers, 0 , len(numbers) - 1)
print(numbers)