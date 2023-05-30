class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def find(self, data):
        if data == self.data:
            return True
        if data < self.data:
            if self.left is not None:
                return self.left.find(data)
        else:
            if self.right is not None:
                return self.right.find(data)
        return False
    
    def print(self, node, level = 0):
        if node.right is not None: self.print(node.right, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.data))
        if node.left is not None: self.print(node.left, level + 1)


root = Node(10)
root.insert(5)
root.insert(15)
root.insert(6)
root.insert(1)
root.insert(8)
root.insert(12)
root.insert(18)
root.insert(17)
print(root.find(6))
print(root.find(7))

root.print(root)

