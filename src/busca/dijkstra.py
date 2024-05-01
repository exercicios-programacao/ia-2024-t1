from util import haversine
import heapq

def dijkstra(graph, start, goal):
    dist = {vertex: float('inf') for vertex in graph.keys()}
    prev = {vertex: None for vertex in graph.keys()}
    dist[start] = 0
    Q = [(0, start)]
    analyzed_nodes = 0

    while Q:
        _, u = heapq.heappop(Q)
        analyzed_nodes += 1
        if u == goal:
            break
        for v, weight in graph[u][1].items():
            alt = dist[u] + weight
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(Q, (alt, v))

    path = []
    current = goal
    while current is not None:
        path.insert(0, current)
        current = prev[current]

    if path[0] != start:
        return analyzed_nodes, float('inf'), []

    path_length = sum(haversine(graph[path[i]][0][0], graph[path[i]][0][1], graph[path[i+1]][0][0], graph[path[i+1]][0][1]) for i in range(len(path) - 1))

    return analyzed_nodes, path_length, path