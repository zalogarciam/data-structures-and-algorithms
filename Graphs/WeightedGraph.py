class WeightedGraph:
    def __init__(self) -> None:
        self.nodes = {}
        self.adjacency_list = {}

    class Node:
        def __init__(self, label) -> None:
            self.label = label
            # self.edges = {}
    
        def __str__(self):
            return f"{self.label}"
        
        # def add_edge(self, destination, weight):
        #     self.edges[destination] = WeightedGraph.Edge(self.label, destination, weight)
    class Edge:
        def __init__(self, source, destination, weight) -> None:
            self.source = WeightedGraph.Node(source)
            self.destination = WeightedGraph.Node(destination)
            self.weight = weight
    
        def __str__(self):
            return f"{self.source} --> {self.destination} ({self.weight})"
        
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

        # current_destination = self.adjacency_list[destination]
        # current_destination.append(self.Edge(source, destination, weight))
        # current_destination.append(self.Edge(destination, source, weight))

    # def add_node_(self, label):
    #     if label not in self.nodes:
    #         self.nodes[label] = self.Node(label)

    # def add_edge_(self, source, destination, weight):
    #     if source not in self.nodes or destination not in self.nodes:
    #         raise Exception('Node does not exist')
    #     self.nodes[source].add_edge(destination, weight)
    #     self.nodes[destination].add_edge(source, weight)

    def print_graph(self):
        for item in self.adjacency_list:
            neighbours = self.adjacency_list[item]
            for neighbour in neighbours:
                print(neighbour)
        print()

    # def print_graph_(self):
    #     for item in self.nodes:
    #         neighbours = self.nodes[item]
    #         for edge in neighbours.edges:
    #             print(neighbours.edges[edge])
    #     print()

graph = WeightedGraph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_edge('A', 'B', 3)
graph.add_edge('A', 'C', 2)
graph.print_graph()

# graph = WeightedGraph()
# graph.add_node_('A')
# graph.add_node_('B')
# graph.add_node_('C')
# graph.add_edge_('A', 'B', 3)
# graph.add_edge_('A', 'C', 2)
# graph.print_graph_()