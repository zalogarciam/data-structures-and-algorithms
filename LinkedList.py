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
            self.index += 1
        else:
            print("Head already added")

    def add_last(self, value):
        if self.tail is None:
            self.tail = Node(value)
            self.head.next = self.tail
            self.index += 1
        else:
            print("Tail already added")


linkedList = LinkedList()
linkedList.add_first(1)
linkedList.add_last(2)
linkedList.print_list()