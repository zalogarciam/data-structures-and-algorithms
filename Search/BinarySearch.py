def binary_search_recursive(array, target):
    return binary_search_recursive_(array, target, 0, len(array) - 1)

def binary_search_recursive_(array, target, left, right):
    if right < left: return -1
    middle = (left + right) // 2
    if array[middle] == target:
        return middle
    if target < array[middle]:
        return binary_search_recursive_(array, target, left, middle - 1)
    return binary_search_recursive_(array, target, middle + 1, right)

# print(binary_search_recursive([1,3,5,6,7], 3))

def binary_search(array, target):
    left = 0 
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        if target < array[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1

print(binary_search([1,3,5,6,7], 3))
