def merge_sort(array):
    if len(array) <= 1: return array

    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]
    # print(left, right)
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    while i < len(left): 
        result.append(left[i])
        i+=1
    while j < len(right): 
        result.append(right[j])
        j+=1
    return result

numbers = [7,3,1,4,6,2,3]
sort = merge_sort(numbers)
print(sort)