class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.eow = False

    def remove_child(self, char):
        self.children.pop(char)

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
    
    def remove(self, word):
        if word is None: return
        self.remove_(self.root, word, 0)


    def remove_(self, node, word, index):
        if index == len(word):
            node.eow = False
            return
        char = word[index]
        child = node.children.get(char, None)
        if child == None:
            return
        self.remove_(child, word, index + 1)
        if len(child.children) == 0 and not child.eow:
            node.children.pop(char)


    def pprint(self):
        self._pprint_helper(self.root, "")

    def _pprint_helper(self, node, prefix):
        if node is None:
            return

        if node.eow:
            print(prefix + "|--", node.value, '(eow)')
        else:
            print(prefix + "|--", node.value)
        prefix = prefix + "|   "

        for child in node.children:
            self._pprint_helper(node.children[child], prefix)

    def traverse(self):
        self.traverse_(self.root)

    def traverse_(self, node):
        print(node.value)
        for item in list(node.children.values()):
            self.traverse_(item)

trie = Trie()
# trie.insert('cat')
trie.insert('car')
trie.insert('care')
# trie.insert('canada')
# print(trie.contains('cat'))
# print(trie.contains('can'))
# print(trie.contains('cam'))
# print(trie.contains('canada'))
# trie.traverse()
trie.pprint()
trie.remove('care')
trie.pprint()
