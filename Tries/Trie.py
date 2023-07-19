class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.eow = False

class Trie:
    def __init__(self) -> None:
        self.root = Node('NULL')

    def insert(self, value):
        current = self.root
        for char in value:
            if (char not in current.children):
                current.children[char] = Node(char)
            current = current.children[char]
        current.eow = True

    def contains(self, word):
        current = self.root
        if word is None: return False
        for char in word:
            if (char not in current.children):
                return False
            else:
               current = current.children[char]
        return current.eow

    def pprint(self):
        self._pprint_helper(self.root, "")

    def _pprint_helper(self, node, prefix):
        if node is None:
            return

        print(prefix + "|--", node.value)
        prefix = prefix + "|   "

        for child in node.children:
            self._pprint_helper(node.children[child], prefix)

trie = Trie()
trie.insert('cat')
trie.insert('canada')
print(trie.contains('cat'))
print(trie.contains('can'))
print(trie.contains('cam'))
print(trie.contains('canada'))

trie.pprint()
