     # Space    O(n + k)
# Time     O(k)  - k buckets
# More buckets, algorithm faster but more memory
# Reduce buckets, algoritms slower but less memory

#                       Best        Worst
# Distribution          O(n)        O(n)
# Iterating Buckets     O(k)        O(k)
# Sorting               O(1)        O(n^2)
# Total                 O(n + k)    O(n^2)

def bucket_sort(array, number_of_buckets):
    index = 0
    for bucket in create_buckets(array, number_of_buckets):
        sorted_bucket = sorted(bucket)
        for item in sorted_bucket:
            array[index] = item
            index +=1

def create_buckets(array, number_of_buckets):
    buckets = [[] for _ in range(number_of_buckets)]
    for item in array:
        buckets[item // number_of_buckets].append(item)
    return buckets


array = [7,1,3,5,3] 
bucket_sort(array, 3)
print(array)