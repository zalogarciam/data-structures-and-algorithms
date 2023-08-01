
class Graph:
    def __init__(self) -> None:
        self.nodes = {}

    class Node:
        def __init__(self, label) -> None:
            self.label = label
            self.neighbors = []

        def has_neighbors(self):
            return len(self.neighbors) > 0
        
        def neighbor_exists(self, node):
            return node in self.neighbors

    def add_node(self, label):
        if label not in self.nodes:
            self.nodes[label] = self.Node(label)

    def remove_node(self, label):
        if label not in self.nodes:
            raise Exception('Node does not exist')
        for node in self.nodes:
            current = self.nodes[node]
            if current.has_neighbors() and current.neighbor_exists(self.nodes[label]):
                self.remove_edge(node, label)
        del self.nodes[label]

    def add_edge(self, source, destination):
        if destination not in self.nodes[source].neighbors:
            self.nodes[source].neighbors.append(self.nodes[destination])

    def remove_edge(self, source, destination):
        if source not in self.nodes or destination not in self.nodes:
            raise Exception('One of the nodes does not exist')
        if self.nodes[destination] in self.nodes[source].neighbors:
            self.nodes[source].neighbors.remove(self.nodes[destination])

    def print_graph(self):
        for node in self.nodes:
            current = self.nodes[node]
            for neighbor in current.neighbors:
                print(self.nodes[node].label, "-->", neighbor.label)
        print()

graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'A')
graph.print_graph()
graph.remove_node('C')
# graph.remove_edge('A', 'C')

graph.print_graph()