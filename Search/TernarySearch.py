def ternary_search(array, target):
    return ternary_search_(array, target, 0, len(array) - 1)
def ternary_search_(array, target, left, right):
    partition_size = (right - left) // 3
    mid1 = left + partition_size
    mid2 = right - partition_size
    if left > right: return -1
    if array[mid1] == target: return mid1
    if array[mid2] == target: return mid2
    if target < array[mid1]: return ternary_search_(array, target, left, mid1 - 1)
    if target > array[mid1]: return ternary_search_(array, target, mid2 + 1, right)
    return ternary_search_(array, target, mid1+1, mid2-1)

print(ternary_search([1,3,5,6,7], 7))