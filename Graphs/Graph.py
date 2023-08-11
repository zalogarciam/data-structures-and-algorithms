
class Graph:
    def __init__(self) -> None:
        self.nodes = {}
        self.adjacency_list = {}

    class Node:
        def __init__(self, label) -> None:
            self.label = label

    def add_node(self, label):
        if label not in self.nodes:
            self.nodes[label] = self.Node(label)
            self.adjacency_list[label] = []

    def remove_node(self, label):
        if label not in self.nodes:
            return
        node = self.nodes[label]
        for key in self.adjacency_list:
            if node in self.adjacency_list[key]:
                self.adjacency_list[key].remove(node)

        del self.adjacency_list[label]
        del self.nodes[label]

    def add_edge(self, source, destination):
        if source not in self.nodes or destination not in self.nodes:
            raise Exception('Node does not exist')
        self.adjacency_list[source].append(self.nodes[destination])

    def remove_edge(self, source, destination):
        if source not in self.nodes or destination not in self.nodes:
            return
        self.adjacency_list[source].remove(self.nodes[destination])

    def print_graph(self):
        for node in self.nodes:
            current = self.nodes[node]
            for neighbor in self.adjacency_list[current.label]:
                print(self.nodes[node].label, "-->", neighbor.label)
        print()

    def dfs_(self, node, visited):
        print(node.label)
        visited.add(node.label)
        for neighbor in self.adjacency_list[node.label]:
            if neighbor.label not in visited:
                self.dfs_(neighbor, visited)

    def dfs(self, label):
        if label not in self.nodes:
            return
        visited = set()
        self.dfs_(self.nodes[label], visited)

    from collections import deque
    
    def dfs_iterative(self, label):
        if label not in self.nodes:
            return
        stack = [label]
        visited = set()
        while len(stack) > 0:
            current = stack.pop()
            if current in visited:
                continue
            print(current)
            visited.add(current)
            neighbors = reversed(self.adjacency_list[current])
            for neighbor in neighbors:
                if neighbor.label not in visited:
                    stack.append(neighbor.label)
        
    def bfs(self, label):
        if label not in self.nodes:
            return
        stack = [label]
        visited = set()
        while len(stack) > 0:
            current = stack.pop(0)
            if current in visited:
                continue
            print(current)
            visited.add(current)
            for neighbor in self.adjacency_list[current]:
                if neighbor.label not in visited:
                    stack.append(neighbor.label)

    # not ok...
    def topological_sort(self, label):
        if label not in self.nodes:
            return
        visited = set()
        stack = []
        sorted = []
        self.topological_sort_(self.nodes[label], visited, stack)
        print(stack)
        while len(stack) > 0:
            sorted.append(stack.pop())
        print(sorted)

    def topological_sort_(self, node, visited, stack):
        visited.add(node.label)
        for neighbor in self.adjacency_list[node.label]:
            if neighbor.label not in visited:
                self.topological_sort_(neighbor, visited, stack)
            # if neighbor.label not in stack:
            #     stack.append(neighbor.label)
        stack.append(node.label)

    def top_sort(self):
        visited = set()
        stack = []
        for label in self.nodes:
            self.top_sort_(label, visited, stack)
            print(visited,stack)
        sorted = []
        while len(stack) > 0:
            sorted.append(stack.pop())
        return sorted

    def top_sort_(self, node, visited, stack):

        if node in visited: return
        visited.add(node)
        for neighbour in self.adjacency_list[node]:
            self.top_sort_(neighbour.label, visited, stack)
        
        stack.append(node)

    def has_cycle(self, label):
        if label not in self.nodes:
            return
        all = set()
        visiting = set()
        visited = set()
     
        return self.has_cycle_(label, visiting, visited)
        
    def has_cycle_(self, label, visiting, visited):
        visited.add(label)
        if label in visiting: return True
        visiting.add(label)
        for neighbour in self.adjacency_list[label]:
            if label not in visited:
                return self.has_cycle_(neighbour.label, visiting, visited)
        return False
        
# Improvement - change neighbors list to dict
graph = Graph()
# graph.add_node('A')
# graph.add_node('B')
# graph.add_node('C')
# graph.add_node('D')
# graph.add_node('E')
# graph.add_edge('A', 'B')
# graph.add_edge('A', 'E')
# graph.add_edge('B', 'E')
# graph.add_edge('C', 'A')
# graph.add_edge('C', 'B')
# graph.add_edge('C', 'D')
# graph.add_edge('D', 'E')
# graph.print_graph()
# graph.dfs('C')
# graph.dfs_iterative('C')
# graph.bfs('C')

# graph.remove_node('A')
# graph.remove_edge('A', 'C')

# graph.print_graph()

# graph.add_node('X')
# graph.add_node('A')
# graph.add_node('B')
# graph.add_node('P')
# graph.add_node('G')
# graph.add_node('H')
# graph.add_node('I')
# graph.add_edge('X', 'A')
# graph.add_edge('X', 'B')
# graph.add_edge('A', 'P')
# graph.add_edge('B', 'P')
# graph.add_edge('P', 'G')
# graph.add_edge('P', 'H')
# graph.add_edge('H', 'I')
# graph.add_edge('I', 'G')
# graph.print_graph()
# print(graph.topological_sort('X'))

# print(graph.top_sort())

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'C')
graph.add_edge('D', 'A')
graph.print_graph()

print(graph.has_cycle('A'))

