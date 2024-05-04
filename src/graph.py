import sys
class Graph:
    def __init__(self, is_direct=False):
        self.nodes = {}
        self.edges = {}
        self.is_direct = is_direct

    def insert_node(self, node, data=None):
        self.nodes[node] = data
        self.edges[node] = {}

    def insert_edge(self, from_node, to_node, cost=0.0):
        if self.edges[from_node] is None:
            self.edges[from_node] = {}

        self.edges[from_node][to_node] = cost

        if not self.is_direct:
            self.edges[to_node][from_node] = cost

    def __len__(self):
        return len(self.edges)

    def get_nodes(self):
        return self.nodes

    def get_neighbors(self, node):
        return self.edges[node]
    
def read_graph(filename: str):
    graph = Graph()
    with open(filename, "rt", encoding="utf-8") as input_file:
        node_count = int(input_file.readline().strip())
        for _ in range(node_count):
            index, latitude, longitude = input_file.readline().strip().split()
            graph.insert_node(int(index), [latitude, longitude])

        edge_count = int(input_file.readline().strip())
        for _ in range(edge_count):
            from_node, to_node, cost = (
                input_file.readline().strip().split()
            )
            graph.insert_edge(int(from_node), int(to_node), float(cost))

    return graph
