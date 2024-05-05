from queue import PriorityQueue
from util import haversine

def a_star(graph, start: int, goal: int) -> (int, float, [int]):
    open_set = PriorityQueue()
    open_set.put(start, 0)
    came_from = {}
    g_score = {}
    came_from[start] = None
    g_score[start] = 0
    explored_nodes = 0 
    
    while not open_set.empty():
        current = open_set.get()

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return (explored_nodes, g_score[goal], path)

        for neighbor, cost in graph[current][1].items():
            tentative_g_score = g_score[current] + cost

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                explored_nodes += 1
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + haversine(
                    graph[goal][0][0],
                    graph[goal][0][1],
                    graph[neighbor][0][0], 
                    graph[neighbor][0][1] 
                )
                open_set.put(neighbor, f_score)
                came_from[neighbor] = current
                
    return (explored_nodes, float('inf'), [])
