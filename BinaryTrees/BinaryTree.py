class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class Tree():
    
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        
        current = self.root
        while (True):
            if (current.data > data):
                if current.left is None:
                    current.left = Node(data)
                    break
                current = current.left

            else:
                if current.right is None:
                    current.right = Node(data)
                    break
                current = current.right

    def find(self, data):
        if self.root.data == data:
            return True
        
        current = self.root
        while (current is not None):
            if current.data == data:
                return True
            if (current.data > data):
                current = current.left
            else:
                current = current.right
        return False
           
    def in_order(self):
         if self.root != None:
            self.in_order(self.root.left)
            print(self.root.data)
            self.in_order(self.root.right)


tree = Tree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(6)
tree.insert(1)
tree.insert(8)
tree.insert(12)
tree.insert(18)
tree.insert(17)
print(tree.find(6))
print(tree.find(7))

# tree.in_order()

