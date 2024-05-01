from util import haversine
from queue import deque

def BFS(graph, start, goal):
    assert(start in graph)
    assert(goal in graph)
    
    visited = set()
    queue = deque([(start, [start])])
    
    while queue:
        v, path = queue.popleft()
        if v == goal:
            path_length = sum(haversine(graph[path[i]][0][0], graph[path[i]][0][1], graph[path[i + 1]][0][0], graph[path[i + 1]][0][1]) for i in range(len(path) - 1))
            return (len(visited), path_length, path)
        
        if v not in visited:
            visited.add(v)  

            for u in graph[v][1]:
                if u not in visited:
                    queue.append((u, path + [u])) 

    return (len(visited), float('inf'), [])