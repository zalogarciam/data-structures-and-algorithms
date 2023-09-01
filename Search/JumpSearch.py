import math
def jump_search(array, target):
    block_size = math.sqrt(len(array))
    start = 0
    next = int(block_size)

    while start < len(array) and array[next-1] < target:
        start = next
        next += int(block_size)
        if next >= len(array): next = len(array)
    for i in range(start, next):
        if array[i] == target:
            return i
    return -1


print(jump_search([1,3,5,6,7], 7))