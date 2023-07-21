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
    
    def contains_recursive_(self, current, word, index):
        if index >= len(word): return current.eow
        char = word[index]
        if (char not in current.children):
            return False
        return self.contains_recursive_(current.children[char], word, index + 1)

    def contains_recursive(self, word):
        if word is None: return False
        return self.contains_recursive_(self.root, word, 0)

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

    def find_words(self, prefix):
        last_node = self.find_last_node_of(prefix)
        list = []
        self.find_words_(last_node, prefix, list)
        return list

    def find_words_(self, node, prefix, list):
        if node is None:
            return
        if node.eow:
            list.append(prefix)
        for child in node.children:
            self.find_words_(node.children[child], prefix + node.children[child].value, list)

    def find_last_node_of(self, prefix):
        if prefix is None: return None
        current = self.root
        for char in prefix:
            child = current.children.get(char, None)
            if child is None:
                return None
            current = child
        return current

    def count_words(self):
        return self.count_words_(self.root)
    
    def count_words_(self, node):
        count = 0
        if node.eow:
            count += 1
        for item in list(node.children.values()):
            count += self.count_words_(item)
        return count

trie = Trie()
# trie.insert('cat')
trie.insert('car')
trie.insert('care')
trie.insert('card')
trie.insert('careful')
trie.insert('egg')
# print(trie.find_words('car'))
# print(trie.contains_recursive('car'))
# print(trie.contains_recursive('cares'))
print(trie.count_words())

# trie.insert('canada')
# print(trie.contains('cat'))
# print(trie.contains('can'))
# print(trie.contains('cam'))
# print(trie.contains('canada'))
# trie.traverse()
# trie.pprint()
# trie.remove('care')
trie.pprint()
