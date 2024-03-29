class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.index = 0

    def print_list(self):
        current = self.head
        linked_list = ""
        while(current is not None):
            if current.next is None:
                linked_list += str(current.value.value)
            else:
                linked_list += str(current.value.value) + "=>"
            current = current.next
        return linked_list

    def add_first(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:  
            new_node.next = self.head
            self.head = new_node
        self.index += 1

    def add_last(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.index += 1

    def delete_first(self):
        if self.is_empty():
            raise Exception("LinkedList is empty")
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            second = self.head.next
            self.head.next = None
            self.head = second
        self.index -= 1

    def delete_last(self):
        last = None
        if self.is_empty():
            raise Exception("LinkedList is empty")
        if self.head == self.tail:
            last = self.head
            self.head = None
            self.tail = None
        else:     
            last = self.tail
            previous = self.get_previous(self.tail)
            self.tail = previous   
            previous.next = None     
        self.index -= 1
        return last.value

    def contains(self, value):
        return self.index_of(value) != -1

    def index_of(self, value):
        count = 0
        current = self.head
        while (current is not None):
            if current.value == value:
                return count
            current = current.next
            count += 1
        return -1

    def is_empty(self):
        return self.head is None

    def get_previous(self, node):
        current = self.head
        while current is not None:
            if current.next == node: return current
            current = current.next
        return None

    def size(self):
        return self.index

    def to_array(self):
        array = []
        current = self.head
        while (current is not None):
            array.append(current.value)
            current = current.next
        return array

    def reverse(self):
        if self.is_empty(): return

        previous = self.head
        current = self.head.next
        while current is not None:
            next = current.next
            current.next = previous
            current = next
            previous = current

        self.tail = self.head
        self.tail.next = None
        self.head = previous
        
    def get_kth_from_the_end(self, k):
        if k <= 0 or self.is_empty(): return
        if k > self.size(): return 
        
        first = self.head
        second = self.head
        for i in range(k):
            second = second.next
        while second is not None:
            first = first.next
            second = second.next
        return first.value
    
    def print_middle(self):
        if self.is_empty(): return
        if self.head.next is None: return self.head.value

        first = self.head
        second = self.head

        while second != self.tail and second.next != self.tail:
            second = second.next.next
            first = first.next
        if second == self.tail:
            return first.value
        else:
            return (first.value, first.next.value)

    def has_loop(self):
        if self.is_empty(): return
        if self.head.next is None: return self.head.value

        first = self.head
        second = self.head
        while second.next.next is not None:
            second = second.next.next
            first = first.next
            if second.next is None:
                return False
            if second.value == first.value:
                return True
        return False


class KeyValuePair():
    def __init__(self, key, value) -> None:
        self.key = key        
        self.value = value
class HashTable():
    def __init__(self, size
    ) -> None:
        self.items = [None] * size
        self.count = 0
        self.size = size

    def put(self, key, value):
        if (self.count < self.size):
            hash_value = self.hash(key)
            key_value = KeyValuePair(key, value)
            if (self.items[hash_value] is None):
                linked_list = LinkedList()
                linked_list.add_last(key_value)
                self.items[hash_value] = linked_list
            else:
                current = self.items[hash_value].head
                while current is not None:
                    print(current.value.key, key)
                    if current.value.key == key:
                        current.value.value = value
                        return
                    current = current.next

                self.items[hash_value].add_last(key_value)
            self.count += 1
        else:
            raise Exception("Hashtable is full")
    
    def hash(self, key):
        return key % self.size
    
    def get(self, key):
        hash_value = self.hash(key)
        if self.items[hash_value] is None:
            raise Exception("Key does not exist")
        head = self.items[hash_value].head
      
        while head is not None:
            key_value = head.value
            if key_value.key == key:
                return key_value.value
            head = head.next
        return None

    def remove(self , key):
        hash_value = self.hash(key)
        linked_list = self.items[hash_value]
        if linked_list is None:
            raise Exception("Key does not exist")
        if linked_list.size() > 1:
            # Check if head is key
            if (linked_list.head.value.key == key):
                linked_list.delete_first()
                return

            # Check if its at the end
            if (linked_list.tail.value.key == key):
                linked_list.delete_last()
                return

            # Check if it is somewhere in the middle
            current = linked_list.head
            while current is not None:
                key_value = current.value
                if key_value.key == key:
                    previous = linked_list.get_previous(current)
                    previous.next = current.next
                    return
                current = current.next
            raise Exception("Key does not exist")
        else:
            self.items[hash_value] = None

    def print(self):
        print("=========PRINT=========")
        for i in range(self.size):
            if self.items[i] is not None:
                print(self.items[i].print_list(), end="\n")

# hashTable = HashTable(5)
# hashTable.put(1, "Gonzalo") 
# hashTable.put(3, "Garcia")
# hashTable.put(4, "Martinez")
# hashTable.put(6, "Juan")
# hashTable.put(6, "Test")

# hashTable.print()
# hashTable.remove(3)
# hashTable.remove(1)
# hashTable.print()
# print("=========GET=========")
# print(hashTable.get(1))
# print(hashTable.get(6))
# print(hashTable.get(2))

def find_first_non_repeated_character(string):
    dict = {}
    for i in string:
        if i != ' ':
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
    for i in dict:
        if dict[i] == 1:
            return i
            
# print(find_first_non_repeated_character('a green apple'))

# my_set = set((1, 1, 2 ,3 ,4, 5 , 6))
# print(my_set)
# print(1 in my_set)

def first_first_repeated_character(string):
    dict = set()
    for i in string:
        if i != ' ':
            if i not in dict:
                dict.add(i)
            else:
                return i

# print(first_first_repeated_character('green apple'))

def hash(number):
    return number % 100

def most_frequent(array):
    dict = {}
    for item in array:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    max = -1
    result = 0
    for key in dict:
        if dict[key] > max:
            max = dict[key]
            result = key
    print(result)

# most_frequent([1,2,2,3,3,3,4])

def count_pairs_with_diff(nums, k):
    num_dict = {}
    count = 0
    
    for num in nums:
        num_dict[num] = num_dict.get(num, 0) + 1
    for num in num_dict:
        if num + k in num_dict:
            count += 1
    
    print(count)

# count_pairs_with_diff([1, 7, 5, 9, 2, 12, 3], 2)

def two_sum(array, target):
    dict = {}
    for index, item in enumerate(array):
        dict[item] = index

    for index, item in enumerate(array):
        if target - item in array:
            print (dict[item], dict[target - item])
            return
    

# two_sum([2, 7, 11, 15], 9)

class HashTableLinearProbing:
    def __init__(self, size
    ) -> None:
        self.items = [None] * size
        self.count = 0
        self.size = size

    def put(self, key, value):
        index = self.hash(key)
        key_value = KeyValuePair(key, value)
        if self.items[index] is None:
            self.items[index] = key_value
        else:
            old_index = index
            while True:
                if index == self.size:
                    index = 0
                if self.items[index] is None:
                    self.items[index] = key_value
                    return
                index += 1
                if index == old_index:
                    raise Exception("Hashtable is full")


    def get(self, key):
        index = self.hash(key)
        old_index = index
        while(True):
            if self.items[index].key == key:
                if self.items[index].value == "TOMBSTONE":
                    return None
                return  self.items[index].value
            index +=1
            if index == self.size:
                index = 0
            if index == old_index:
                    raise Exception("Item not found")

    def remove(self, key):
        index = self.hash(key)
        while (True):
            if self.items[index].key == key:
                self.items[index].value = "TOMBSTONE" 
                return  
            index+=1 

    def size(self):
        return self.size
    
    def hash(self, number):
        return number % self.size
    
    def print(self):
        for item in self.items:
            print(item.value, end=" ")
    
hash_probing = HashTableLinearProbing(5)
hash_probing.put(6, 'A')
hash_probing.put(11, 'C')
hash_probing.put(8, 'B')
hash_probing.put(16, 'D')
hash_probing.put(21, 'E')
# hash_probing.put(26, 'F')
hash_probing.print()
print()
print(hash_probing.get(8))
hash_probing.remove(11)
hash_probing.print()
print()
print("======GET======")
print(hash_probing.get(21))
print(hash_probing.get(1))



