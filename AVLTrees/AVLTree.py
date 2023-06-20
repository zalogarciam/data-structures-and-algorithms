class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data, root):
        if self.root is None:
            self.root = Node(data)
            return
        
        current = root
        if (current.data > data):
            if current.left is None:
                current.left = Node(data)
                return
            self.insert(data, root.left)

        else:
            if current.right is None:
                current.right = Node(data)
                return
            self.insert(data, root.right)

    def in_order_level(self, root, level = 1):
         if root != None:
            self.in_order_level(root.left, level + 1)
            print(level * 4 * "-" + str(root.data))
            self.in_order_level(root.right, level + 1)
# 1 2 3 4 5
# L L

# 5 10 3 12 15 14
# L L

# 12, 3, 9, 4, 6, 2
# LR L L

avlTree = AVLTree()
avlTree.insert(12, avlTree.root)
avlTree.insert(3, avlTree.root)
avlTree.insert(9, avlTree.root)
avlTree.in_order_level(avlTree.root, 1)