from queue import PriorityQueue

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(graph, start: int, goal: int):
    assert(start in graph)
    assert(goal in graph)

    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    nodes_analyzed = 0
    
    while not frontier.empty():
        current = frontier.get()
        nodes_analyzed += 1
        
        if current == goal:
            break

        for next in graph[current][1].keys():
            new_cost = cost_so_far[current] + graph[current][1][next]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(graph[current][0], graph[next][0])
                frontier.put(next, priority)
                came_from[next] = current

    if current != goal:
        return nodes_analyzed, float('inf'), []

    path = []
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    
    return nodes_analyzed, cost_so_far[goal], path

