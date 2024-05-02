from queue import PriorityQueue

def a_star(graph, start, goal):
    def heuristic(a, b):
        ax, ay = a['coordinates']
        bx, by = b['coordinates']
        return abs(ax - bx) + abs(ay - by)
    
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break

        for next_node, cost in graph[current]['edges'].items():
            new_cost = cost_so_far[current] + cost
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(graph[start], graph[goal])
                frontier.put(next_node, priority)
                came_from[next_node] = current
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    
    return len(path), cost_so_far[goal], path