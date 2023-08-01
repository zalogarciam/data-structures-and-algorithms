
class Graph:
    def __init__(self) -> None:
        self.nodes = {}

    class Node:
        def __init__(self, label) -> None:
            self.label = label
            self.neighbors = []

    def add_node(self, label):
        pass

    def remove(self, label):
        pass

    def add_edge(self, source, destination):
        pass

    def remove_edge(self, source, destination):
        pass

    def print_graph(self):
        pass