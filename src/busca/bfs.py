class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def purge(self):
        self.items = []


def bfs(graph, source: int, goal: int) -> (int, float, [int]):
    visited_count = 0
    total_length = 0.0
    path = []

    queue = Queue()
    queue.enqueue(source)

    visited_nodes = {}
    for node in graph.get_nodes():
        visited_nodes[node] = 0

    visited_nodes[source] = 1  

    while not queue.is_empty():
        u = queue.dequeue()

        path.append(u)

        if u == goal:
            return (visited_count, total_length, path)

        visited_count += 1

        neighbors = graph.get_neighbors(u)

        for neighbor in neighbors.keys():
            if visited_nodes[neighbor] == 0:

                if neighbor == goal:
                    path.append(neighbor)

                    return (visited_count, total_length, path)

                visited_nodes[neighbor] = 1     
                queue.enqueue(neighbor)

    return None
