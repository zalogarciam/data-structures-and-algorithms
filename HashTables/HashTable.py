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
                linked_list += str(current.value)
            else:
                linked_list += str(current.value) + "=>"
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
    def __init__(self) -> None:
        self.key = None        
        self.value = LinkedList()
class HashTable():
    def __init__(self) -> None:
        self.items = []
        self.count = 0

    def put(self, key, value):
        if (self.exist(key)):
            index = self.index_of(key)
            self.items[index].value.add_last(value)
        else:
            key_value = KeyValuePair()
            key_value.key = key
            key_value.value.add_last(value)
            self.items.append(key_value)
            self.count += 1
    
    def exist(self, key):
        for item in self.items:
            if item.key == key: return True
        return False

    def index_of(self, key):
        for index in range(len(self.items)):
            if self.items[index].key == key: return index

    def get(self, key):
        for item in self.items:
            if item.key == key: return item.value
        return None

    def remove(self , key):
        for item in self.items:
            if item.key == key: 
                self.items.remove(item)
                return True
        return False

    def print(self):
        for item in self.items:
            print("Key: " + str(item.key) + " Value: " + item.value.print_list(), end="\n")

hashTable = HashTable()
hashTable.put(0, "Gonzalo")
hashTable.put(1, "Enrique")
hashTable.put(2, "Garcia")
hashTable.put(3, "Martinez")
hashTable.put(2, "Juan")
print(hashTable.get(3).print_list())
print(hashTable.get(2).print_list())
hashTable.print()
hashTable.remove(2)
hashTable.print()

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


