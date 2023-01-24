# Lookup O(n)
# Lookup by index O(n)
# Insert at the end O(1) and insert at the start too    
# Insert in the middle O(n)
# Delete at the start is O(1) and O(n) if its end, if its in the middle O(n)

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
        print(linked_list)

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
        if self.is_empty():
            raise Exception("LinkedList is empty")
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:     
            previous = self.get_previous(self.tail)
            self.tail = previous   
            previous.next = None     
        self.index -= 1

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

linkedList = LinkedList()
linkedList.add_first(1)
linkedList.add_last(2)
linkedList.add_last(3)
linkedList.add_last(4)
linkedList.add_last(5)
linkedList.add_last(6)
linkedList.add_first(0)

linkedList.add_first(-1)
linkedList.add_last(5)
linkedList.print_list()
linkedList.delete_first()
linkedList.delete_last()
print(linkedList.contains(3))
print(linkedList.contains(0))
print(linkedList.index_of(3))
print(linkedList.index_of(0))
linkedList.size()
print(linkedList.to_array())
linkedList.reverse()
linkedList.print_list()
print(linkedList.print_middle())
print(linkedList.get_kth_from_the_end(3))

print(linkedList.tail.value)
print(linkedList.head.next.next.next.value)
linkedList.tail.next = linkedList.head.next.next.next
print(linkedList.has_loop())