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
        return self.head == None

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

class LinkedListStack(LinkedList):
    def __init__(self):
        super().__init__()

    def push(self, value):
        self.add_last(value)

    def pop(self):
        return self.delete_last()

    def peek(self):
        return self.tail.value

    def empty(self):
        return self.is_empty()

    def print_stack(self):
        self.print_list()

    def min(self):
        return self.minimum 


class MinStack():
    def __init__(self):
        self.stack = LinkedListStack()
        self.min_stack = LinkedListStack()

    def push_(self, value):
        self.stack.push(value)
        if self.min_stack.empty():
            self.min_stack.push(value)
        else:
            if self.min_stack.peek() > value:
                self.min_stack.push(value)

    def pop_(self):
        top = self.stack.pop()
        if top == self.min_stack.peek():
            self.min_stack.pop()
        return top

    def min(self):
        return self.min_stack.peek()

stack = MinStack()
stack.push_(5)
stack.push_(2)
stack.push_(10)
stack.push_(1)
print(stack.min())
stack.pop_()
print(stack.min())
