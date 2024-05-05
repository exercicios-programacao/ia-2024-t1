def dijkstra(graph, start, goal):
    dist = {node: float('inf') for node in graph.nodes}
    dist[start] = 0  

    visited = set()  

    while len(visited) < len(graph.nodes):
        min_dist_node = min((node for node in graph.nodes if node not in visited), key=lambda x: dist[x])

        visited.add(min_dist_node)

        for neighbor in graph.neighbors(min_dist_node):
            if neighbor not in visited:
                new_dist = dist[min_dist_node] + graph.distance(min_dist_node, neighbor)
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist

    return dist[goal], shortest_path(start, goal, dist)

def shortest_path(start, goal, dist, graph):
    path = [goal]
    while path[-1] != start:
        neighbors = graph.neighbors(path[-1])
        prev_node = min(neighbors, key=lambda x: dist[x])
        path.append(prev_node)
    return path[::-1]
