
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
# Improvement - change neighbors list to dict
graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'A')
graph.print_graph()
graph.remove_node('A')
# graph.remove_edge('A', 'C')

graph.print_graph()