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
           
    def in_order(self, root):
         if root != None:
            self.in_order(root.left)
            print(root.data)
            self.in_order(root.right)

    def pre_order(self, root):
        if root is not None:
            print(root.data)
            self.pre_order(root.left)
            self.pre_order(root.right)

    def pos_order(self, root):
        if root is not None:
            self.pre_order(root.left)
            self.pre_order(root.right)
            print(root.data)

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

tree.pre_order(tree.root)
tree.in_order(tree.root)
tree.pos_order(tree.root)

#Exercise
# BFS: 20 10 30 6 14 24 3 8 26
# PRE (ROOT, LEFT, RIGHT): 20 10 6 3 8 14 30 24 26
# IN (LEFT, ROOT, RIGHT):  3 6 8 10 14 20 24 26 30
# POS (LEFT, RIGHT, ROOT): 3 8 6 14 10 26 24 30 20