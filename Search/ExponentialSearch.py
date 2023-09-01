def binary_search_recursive_(array, target, left, right):
    if right < left: return -1
    middle = (left + right) // 2
    if array[middle] == target:
        return middle
    if target < array[middle]:
        return binary_search_recursive_(array, target, left, middle - 1)
    return binary_search_recursive_(array, target, middle + 1, right)

def exponential_search(array, target):
    bound = 1

    while (bound < len(array) and array[bound] < target):
        bound *= 2

    left = bound // 2
    right = min(bound , len(array) - 1)
    return binary_search_recursive_(array, target, left ,right)

print(exponential_search([1,3,5,6,7], 7))