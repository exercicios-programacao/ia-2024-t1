class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


def dfs(graph, source: int, goal: int) -> (int, float, [int]):
    visited_count = 0
    total_length = 0.0
    path = []

    stack = Stack()
    stack.push(source)

    visited_nodes = {}
    for node in graph.get_nodes():
        visited_nodes[node] = 0

    visited_nodes[source] = 1  # visited

    while not stack.is_empty():
        u = stack.pop()
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

                visited_nodes[neighbor] = 1  # visited
                stack.push(neighbor)

    return None
