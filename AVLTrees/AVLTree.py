class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = None

class AVLTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        self.root = self._insert(data, self.root)

    def _insert(self, data, root):
        if root is None:
            return Node(data)
        
        if (root.data > data):
            root.left = self._insert(data, root.left)
        else:
            root.right = self._insert(data, root.right)

        root.height = self.set_height(root)
      
        return self.balance(root)
    
    def rotate_left(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        self.set_height(root)
        self.set_height(new_root)
        return new_root

    def rotate_right(self, root):
        new_root= root.left
        root.left = new_root.right
        new_root.right = root
        self.set_height(root)
        self.set_height(new_root)
        return new_root

    def set_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left) if node.left else -1
        right_height = self.height(node.right) if node.right else -1
        return max(left_height, right_height) + 1
    
    def left_heavy(self, node):
        return self.balance_factor(node) > 1
    
    def right_heavy(self, node):
        return self.balance_factor(node) < -1
    
    def balance(self, root):
        balance = self.balance_factor(root)
        if self.left_heavy(root):
            # print("Left heavy: ", balance)
            if (self.balance_factor(root.left) < 0):
                root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        elif self.right_heavy(root):
            # print("Right heavy: " , balance)
            if (self.balance_factor(root.right) > 0):
                 root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root
    
    def balance_factor(self, node):
        if node is None: return 0
        else: return self.height(node.left) - self.height(node.right)

    def in_order_level(self, root, level = 1):
         if root != None:
            self.in_order_level(root.left, level + 1)
            print(level * 4 * "-" + str(root.data) + " ("+str(root.height)+")" )
            self.in_order_level(root.right, level + 1)
# 1 2 3 4 5
# L L

# 5 10 3 12 15 14
# L L

# 12, 3, 9, 4, 6, 2
# LR L L

avlTree = AVLTree()
avlTree.insert(10)
avlTree.insert(30)
avlTree.insert(20)

avlTree.in_order_level(avlTree.root, 1)