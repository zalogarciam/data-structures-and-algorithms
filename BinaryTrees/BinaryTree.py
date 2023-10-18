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

    def remove(self, root, data):
        if not root:
            return root
        if root.data > data:
            root.left = self.remove(root.left, data)
        elif root.data < data:
            root.right = self.remove(root.right, data)
        else:
            if root.right is None:
                return root.left
            if root.left is None:
                return root.right
            # If both left and right children exist in the node replace its value with
            # the minmimum value in the right subtree. Now delete that minimum node
            # in the right subtree
            tmp = self.min(root.right)
            root.data = tmp.data
            root.right = self.remove(root.right, tmp.data)
        return root

    def min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

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

    def in_order_level(self, root, level = 1):
         if root != None:
            self.in_order_level(root.left, level + 1)
            print(level * 4 * "-" + str(root.data))
            self.in_order_level(root.right, level + 1)

    def pre_order(self, root):
        if root is not None:
            print(root.data)
            self.pre_order(root.left)
            self.pre_order(root.right)

    def pos_order(self, root):
        if root is not None:
            self.pos_order(root.left)
            self.pos_order(root.right)
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
    
    def validate_bst(self, root, start, end):
        if root is None: return True
        if root.data > start and root.data < end:
            return self.validate_bst(root.left, start, root.data) and self.validate_bst(root.right, root.data, end)
        return False
    
    def swap_root(self):
        temp = self.root.left
        self.root.left = self.root.right
        self.root.right = temp

    def nodes_at_k_distance(self, root, k):
        if k == 0 and root is not None: 
            print(root.data)
        if root is None: return True
        return self.nodes_at_k_distance(root.left, k - 1) and self.nodes_at_k_distance(root.right, k -1)
    
    def get_nodes_at_distance(self, root, k):
        list = []
        self.print_nodes_at_distance(root, k, list)
        return list

    def print_nodes_at_distance(self, root, k, list):
        if root is None: return
        if k == 0: 
            list.append(root.data)
            return
        self.print_nodes_at_distance(root.left, k -1, list)
        self.print_nodes_at_distance(root.right, k -1, list)

    def traverse_level_order(self):
        for i in range(self.height(self.root) + 1):
            list = self.get_nodes_at_distance(self.root, i)
            for i in list:
                print(i)

    def bfs(self, root):
        if root is None:
            return
        queue = [root]
        visited = []
        while len(queue) > 0:
            
            current = queue.pop(0)
            if current.data not in visited:
                visited.append(current.data)
            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)
        print(visited)

    def size(self, root):
        if root is None: return 0
        return 1 + max(self.size(root.left), self.size(root.right))

    def size_(self, root):
        if (root == None):
            return 0

        if root.right is None and root.left is None:
            return 1

        return 1 + self.size_(root.left) + self.size_(root.right)
  
    def count_leaves(self, root):
        if root is None: return 0
        if root.left is None and root.right is None:
            return 1
        return self.count_leaves(root.left) + self.count_leaves(root.right)
        
    def max_value(self, root):
        if root is None: return
        current = root
        last = None
        while current is not None:
            last = current
            current = current.right
        return last.data

    def contains(self, root, data):
        current = root

        while current is not None:
            if current.data == data:
                return True
            if data < current.data:
                current = current.left
            else:
                current = current.right
        return False


    def are_siblings(self, root, a, b):
        if root is None: 
            return False
     
        siblings = False
        if root.left is not None and root.right is not None:
            siblings = (root.left.data == a and root.right.data == b) or (root.left.data == b and root.right.data == a)
        
        return siblings or self.are_siblings(root.left,a , b) or self.are_siblings(root.right,a ,b)

    def get_ancestors(self, root, target):
        if root is None:
            return False
        if root.data == target:
            return True
        left = self.get_ancestors(root.left, target)
        right = self.get_ancestors(root.right, target)
        if left or right:
            print(root.data)
            return True
        return False
        
    def invert(self, root):
        if (root == None):
            return root

        left = self.invert(root.left)
        right = self.invert(root.right)

        root.left = right
        root.right = left
        return root

tree = Tree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(6)
tree.insert(1)
tree.insert(8)
tree.insert(12)
tree.insert(13)
tree.insert(11)
tree.insert(18)
tree.insert(20)
tree.insert(17)
tree.in_order_level(tree.root)

tree.remove(tree.root, 15)
tree.in_order_level(tree.root)
# tree_to_invert = Tree()
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.right.left = Node(4)
# # root.left.right = Node(5)
# tree_to_invert.root = root
# tree_to_invert.in_order_level(tree_to_invert.root)
# inverted_root = tree_to_invert.invert(tree_to_invert.root)
# tree_to_invert.in_order_level(inverted_root)

# print(tree.find(6))
# print(tree.find(7))

# tree.pre_order(tree.root)
# tree.in_order(tree.root)
# tree.pos_order(tree.root)
# print('Height: ', tree.height(tree.root))
# print('Min: ', tree.min_value(tree.root))
# print('Min BST: ', tree.min_bst(tree.root))

#Exercise
# BFS: 20 10 30 6 14 24 3 8 26
# PRE (ROOT, LEFT, RIGHT): 20 10 6 3 8 14 30 24 26
# IN (LEFT, ROOT, RIGHT):  3 6 8 10 14 20 24 26 30
# POS (LEFT, RIGHT, ROOT): 3 8 6 14 10 26 24 30 20

# tree2 = Tree()
# tree2.insert(10)
# tree2.insert(5)
# tree2.insert(15)
# tree2.insert(6)
# tree2.insert(1)
# tree2.insert(8)
# tree2.insert(12)
# tree2.insert(18)
# tree2.insert(17)

# print(tree2.equals(tree.root, tree2.root))

# tree3 = Tree()
# tree3.insert(20)
# tree3.insert(10)
# tree3.insert(30)
# tree3.insert(6)
# tree3.insert(21)
# tree3.insert(4)
# tree3.insert(3)
# tree3.insert(8)
# tree3.in_order_level(tree3.root)
# print(tree3.height(tree3.root))
# print(tree3.size_(tree3.root))

# print('Leaves', tree3.count_leaves(tree3.root))
# print('Max: ', tree3.max_value(tree3.root))
# print('Contains: ', tree3.contains(tree3.root, 8))
# print('Contains: ', tree3.contains(tree3.root, 11))
# print('Siblings: ', tree3.are_siblings(tree3.root, 8, 4))
# print('Siblings: ', tree3.are_siblings(tree3.root, 6, 21))

# tree.pre_order(tree.root)
# tree.in_order(tree.root)
# tree.in_order_level(tree.root, 1)
# tree.pos_order(tree.root)
# tree.get_ancestors(tree.root, 8)

# tree3.swap_root()
# print(tree.validate_bst(tree3.root, -float('inf'), float('inf')))
# print(tree3.validate_bst(tree3.root, -float('inf'), float('inf')))
# tree3.nodes_at_k_distance(tree3.root, 3)
# tree3.print_nodes_at_distance(tree3.root, 3)
# print(tree.get_nodes_at_distance(tree.root, 3))
# tree3.traverse_level_order()
# tree3.bfs(tree3.root)