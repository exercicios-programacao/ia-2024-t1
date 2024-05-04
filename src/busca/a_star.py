from typing import List, Tuple
from graph import Vertex

def a_star(graph: List[Vertex], start: int, goal: int) -> Tuple[int, float, List[int]]:
    open_set = {start}
    closed_set = set()
    came_from = {}
    g_score = {vertex.Vertex: float('inf') for vertex in graph}
    g_score[start] = 0
    f_score = {vertex.Vertex: float('inf') for vertex in graph}
    f_score[start] = manhattan_distance((graph[start].Coordinate.Latitude, graph[start].Coordinate.Longitude),
                                        (graph[goal].Coordinate.Latitude, graph[goal].Coordinate.Longitude))

    while open_set:
        current = min(open_set, key=lambda v: f_score[v])
        if current == goal:
            path = []
            while current in came_from:
                path.insert(0, current)
                current = came_from[current]
            return len(closed_set), g_score[goal], [start] + path

        open_set.remove(current)
        closed_set.add(current)

        for neighbor in graph[current].AdjacentVertexList:
            if neighbor.Vertex in closed_set:
                continue

            tentative_g_score = g_score[current] + neighbor.Cost
            if tentative_g_score < g_score[neighbor.Vertex]:
                came_from[neighbor.Vertex] = current
                g_score[neighbor.Vertex] = tentative_g_score
                f_score[neighbor.Vertex] = tentative_g_score + manhattan_distance(
                    (graph[neighbor.Vertex].Coordinate.Latitude, graph[neighbor.Vertex].Coordinate.Longitude),
                    (graph[goal].Coordinate.Latitude, graph[goal].Coordinate.Longitude))
                if neighbor.Vertex not in open_set:
                    open_set.add(neighbor.Vertex)

    return 0, float('inf'), []
