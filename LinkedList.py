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
        while(current is not None):
            print(current.value)
            current = current.next

    def add_first(self, value):
        if self.head is None:
            self.head = Node(value)
        else:  
            new_head = Node(value)
            new_head.next = self.head
            self.head = new_head
        self.index += 1

    def add_last(self, value):
        if self.tail is None:
            self.tail = Node(value)
            self.head.next = self.tail
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.index += 1


    def delete_first(self):
        self.head = self.head.next
        self.index -= 1

    def delete_last(self):
        current = self.head
        while(current.next.next is not None):
            current = current.next
        current.next = None
        self.tail = current        
        self.index -= 1

    def contains(self, value):
        current = self.head
        while(current is not None):
            if current.value == value:
                return True
            current = current.next
        return False

    def indexOf(self, value):
        count = 0
        current = self.head
        while (current is not None):
            if current.value == value:
                return count
            current = current.next
            count += 1
        return -1

linkedList = LinkedList()
linkedList.add_first(1)
linkedList.add_last(2)
linkedList.add_last(3)
linkedList.add_last(4)
linkedList.add_first(0)
linkedList.add_last(5)
linkedList.delete_first()
linkedList.delete_last()
linkedList.print_list()
print(linkedList.contains(3))
print(linkedList.contains(0))
print(linkedList.indexOf(3))
print(linkedList.indexOf(0))