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

    def height(self, root):
        if root is None: return -1
        return 1 + max(self.height(root.left), self.height(root.right))
    
    def min_value(self, root):
        if root is None: 
            return float('inf')

        left = self.min_value(root.left)
        right = self.min_value(root.right)
        return min(left, right, root.data)
    
    def min_bst(self, root):
        if root is None: return
        current = root
        last = None
        while (current is not None):
            last = current
            current = current.left
        return last.data

    def equals(self, node1, node2):
        if node1 is None and node2 is None: return True
        if node1 is not None and node2 is not None:
            return node1.data == node2.data and self.equals(node1.left, node2.left) and self.equals(node1.right, node2.right)
        return False

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

# tree.pre_order(tree.root)
# tree.in_order(tree.root)
# tree.pos_order(tree.root)
print('Height: ', tree.height(tree.root))
print('Min: ', tree.min_value(tree.root))
print('Min BST: ', tree.min_bst(tree.root))

#Exercise
# BFS: 20 10 30 6 14 24 3 8 26
# PRE (ROOT, LEFT, RIGHT): 20 10 6 3 8 14 30 24 26
# IN (LEFT, ROOT, RIGHT):  3 6 8 10 14 20 24 26 30
# POS (LEFT, RIGHT, ROOT): 3 8 6 14 10 26 24 30 20

tree2 = Tree()
tree2.insert(10)
tree2.insert(5)
tree2.insert(15)
tree2.insert(6)
tree2.insert(1)
tree2.insert(8)
tree2.insert(12)
tree2.insert(18)
tree2.insert(17)

print(tree2.equals(tree.root, tree2.root))