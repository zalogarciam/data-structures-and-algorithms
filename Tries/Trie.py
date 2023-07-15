class Node:
    def __init__(self, value):
        self.value = value
        self.children = [None] * 26
        self.eow = False

    def get_children(self):
        children = []
        for child in self.children:
            if child is not None:
                children.append(child.value)
        return children

class Trie:
    def __init__(self) -> None:
        self.root = Node(None)

    def insert(self, value):
        current = self.root
        for char in value:
            index = ord(char) - ord('a')
            if char in current.get_children():
                current = current.children[index]
                continue
            current.children[index] = Node(char)
            if value[len(value) - 1] == char:
                current.children[index].eow = True
                break

            current = current.children[index]

    def pprint(self):
        self._pprint_helper(self.root, "")

    def _pprint_helper(self, node, prefix):
        if node is None:
            return

        print(prefix + "|--", node.value)
        prefix = prefix + "|   "

        for child in node.children:
            self._pprint_helper(child, prefix)

trie = Trie()
trie.insert('cat')
trie.insert('can')
trie.pprint()
