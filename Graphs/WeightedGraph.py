class WeightedGraph:
    def __init__(self) -> None:
        self.nodes = {}
        self.adjacency_list = {}

    class Node:
        def __init__(self, label) -> None:
            self.label = label

    class Edge:
        def __init__(self, source, destination, weight) -> None:
            self.source = WeightedGraph.Node(source)
            self.destination = WeightedGraph.Node(destination)
            self.weight = weight
    
    def add_node(self, label):
        if label not in self.nodes:
            self.nodes[label] = self.Node(label)
            self.adjacency_list[label] = []

    def add_edge(self, source, destination, weight):
        if source not in self.nodes or destination not in self.nodes:
            raise Exception('Node does not exist')
        current_source = self.adjacency_list[source]
        current_source.append(self.Edge(source, destination, weight))
        current_source.append(self.Edge(destination, source, weight))

        current_destination = self.adjacency_list[destination]
        current_destination.append(self.Edge(source, destination, weight))
        current_destination.append(self.Edge(destination, source, weight))

    def print_graph(self):
        for item in self.adjacency_list:
            neighbours = self.adjacency_list[item]
            for neighbour in neighbours:
                print(neighbour.source.label, "-->", neighbour.destination.label, '(', neighbour.weight, ')')
        print()

graph = WeightedGraph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_edge('A', 'B', 3)
graph.add_edge('A', 'C', 7)
graph.add_edge('A', 'D', 5)
graph.add_edge('B', 'D', 1)
graph.print_graph()