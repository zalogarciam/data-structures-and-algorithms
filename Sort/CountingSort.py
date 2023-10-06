#               Best      
# Time          O(n) + O(k) = O(n)
# Space         O(k)

def counting_sort(array, max):
    counts = [0] * (max + 1)
    for item in array:
        counts[item] += 1

    k = 0
    for i in range(len(counts)):
        for j in range(counts[i]):
            array[k] = i
            k += 1

array = [5,3,2,5,4,4,5] 
counting_sort(array, max(array))
print(array)