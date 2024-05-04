"""Implementação do algoritmo A*."""
import heapq

def heuristic(node, goal, graph):
    """Busca por heuristica."""
    for edge in graph[node]['edges']:
        if edge[0] == goal:
            return edge[1]
    return float('inf')

def a_star(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando A*."""

    if goal not in graph:
        raise ValueError("Goal doesn't exist in this graph")

    open_list = [(0, start)] # tuple data (f_cost, node)
    came_from = {} # total path
    g_cost = {node: float('inf') for node in graph} # final cost
    g_cost[start] = 0
    f_cost = {node: float('inf') for node in graph} # final cost with heuristic cost
    f_cost[start] = heuristic(start, goal, graph)

    while open_list:
        current_f_cost, current_node = heapq.heappop(open_list) # smaller coaster of list

        if current_node == goal:
            path = [] # remake the path
            while current_node in came_from:
                path.insert(0, current_node)
                current_node = came_from[current_node]
            path.insert(0, start)
            return len(path), f_cost[goal], path

        for neighbor, cost in graph[current_node]['edges']:
            # calculate current cost from start to neighbor through current node
            tentative_g_cost = g_cost[current_node] + cost

            if tentative_g_cost < g_cost[neighbor]:
                came_from[neighbor] = current_node
                g_cost[neighbor] = tentative_g_cost
                f_cost[neighbor] = g_cost[neighbor] + heuristic(neighbor, goal, graph)
                heapq.heappush(open_list, (f_cost[neighbor], neighbor))

    raise ValueError("Goal node is not reachable from the start node")
