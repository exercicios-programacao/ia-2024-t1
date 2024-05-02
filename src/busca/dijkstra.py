from heapq import heappush, heappop

def dijkstra(graph, source, goal):
    dist = {v: float('inf') for v in graph.keys()}
    prev = {v: None for v in graph.keys()}
    dist[source] = 0
    
    Q = [(0, source)]
    analyzed_nodes = set()
    
    while Q:
        _, u = heappop(Q)
        analyzed_nodes.add(u)
        
        if u == goal:
            path = []
            current = goal
            while current is not None:
                path.append(current)
                current = prev[current]
            path.reverse()
            return len(analyzed_nodes), dist[goal], path
        
        for v, w in graph[u]['edges'].items():
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heappush(Q, (dist[v], v))
    
    return len(analyzed_nodes), float('inf'), []