class Path:
    def __init__(self) -> None:
        self.list = []

class WeightedGraph:
    def __init__(self) -> None:
        self.nodes = {}
        self.edges = {}

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
            self.edges[label] = []

    def add_edge(self, source, destination, weight):
        if source not in self.nodes or destination not in self.nodes:
            raise Exception('Node does not exist')
        current_source = self.edges[source]
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
        for item in self.edges:
            neighbours = self.edges[item]
            for neighbour in neighbours:
                print(neighbour)
        print()

    # def print_graph_(self):
    #     for item in self.nodes:
    #         neighbours = self.nodes[item]
    #         for edge in neighbours.edges:
    #             print(neighbours.edges[edge])
    #     print()

    def get_shortest_distance(self, source, destination):
        distances = {}
        for node in self.nodes:
            distances[node] = float('inf')
        distances[source] = 0

        visited = []
        queue = [(0, source)]

        while (len(queue) > 0):
            current = queue.pop(0)[1]
            visited.append(current)

            for edge in self.edges[current]:
                if edge.destination.label in visited:
                    continue
                new_distance = distances[current] + edge.weight
                if new_distance < distances[edge.destination.label]:
                    distances[edge.destination.label] = new_distance
                    queue.append((new_distance, edge.destination.label))

        print(distances[destination])
        return distances[destination]

    def get_shortest_path(self, source, destination):
        if source not in self.nodes or destination not in self.nodes:
            raise Exception("Node does not exist")
        distances = {}
        for node in self.nodes:
            distances[node] = float('inf')
        distances[source] = 0

        previous_nodes = {}
        visited = []
        queue = [(0, source)]

        while (len(queue) > 0):
            current = queue.pop(0)[1]
            visited.append(current)

            for edge in self.edges[current]:
                if edge.destination.label in visited:
                    continue
                new_distance = distances[current] + edge.weight
                if new_distance < distances[edge.destination.label]:
                    distances[edge.destination.label] = new_distance
                    previous_nodes[edge.destination.label] = current
                    queue.append((new_distance, edge.destination.label))

        return self.build_path(destination, previous_nodes)
    
    def build_path(self, destination, previous_nodes):
        stack = [self.nodes[destination].label]
        previous = previous_nodes[destination]
        while (previous is not None):
            stack.append(previous)
            if previous not in previous_nodes:
                break
            previous = previous_nodes[previous]

        path = Path()
        while (len(stack)> 0):
            path.list.append(stack.pop())
        return path.list

    def has_cycle_(self, node, parent, visited):
        visited.append(node)

        for edge in self.edges[node.label]:
            if edge.destination == parent:
                continue
            if edge.destination in visited or self.has_cycle_(edge.destination, node, visited):
                return True

        return False
        
    # Only on directed graphs
    def has_cycle(self):
        visited = []
        for node in self.nodes:
            if node not in visited and self.has_cycle_(self.nodes[node], None, visited):
                return True
        return False
            
graph = WeightedGraph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_edge('A', 'B', 1)
# graph.add_edge('B', 'C', 2)
# graph.add_edge('C', 'A', 10)
graph.print_graph()
# print(graph.get_shortest_path('A', 'C'))
print(graph.has_cycle())

# graph = WeightedGraph()
# graph.add_node_('A')
# graph.add_node_('B')
# graph.add_node_('C')
# graph.add_edge_('A', 'B', 3)
# graph.add_edge_('A', 'C', 2)
# graph.print_graph_()