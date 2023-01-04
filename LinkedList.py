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

    def print_list(self):
        current = self.head
        while(current is not None):
            print(current.value)
            current = current.next


linkedList = LinkedList()
linkedList.head = Node(5)
linkedList.tail = Node(6)
linkedList.head.next = linkedList.tail
linkedList.print_list()