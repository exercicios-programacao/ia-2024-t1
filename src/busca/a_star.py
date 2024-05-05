def a_star(graph, start, goal):
    open_set = [(0, start)] 
    came_from = {}  
    g_score = {node: float('inf') for node in graph.nodes}  
    g_score[start] = 0  
    f_score = {node: float('inf') for node in graph.nodes}
    f_score[start] = heuristic_cost_estimate(start, goal)  

    while open_set:
        current_f, current = min(open_set)

        if current == goal:
            return reconstruct_path(came_from, goal)

        open_set.remove((current_f, current))

        for neighbor in graph.neighbors(current):
            tentative_g_score = g_score[current] + graph.distance(current, neighbor)
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic_cost_estimate(neighbor, goal)
                if neighbor not in [node for _, node in open_set]:
                    open_set.append((f_score[neighbor], neighbor))

    return None

def heuristic_cost_estimate(node, goal, graph):
    return graph.distance(node, goal)

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]  
