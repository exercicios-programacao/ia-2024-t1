from collections import deque

def bfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em largura."""

    queue = deque([(start, None)])
    visited = {} 
    count_nodes = 0

    while queue:
        current_node, predecessor = queue.popleft() 
        count_nodes += 1

        if current_node == goal:
            path = [current_node]
            total_cost = 0
            while predecessor is not None:
                path.append(predecessor)
                total_cost += graph[predecessor][1][current_node]
                current_node = predecessor
                predecessor = visited.get(current_node)
            path.reverse()
            return (count_nodes, total_cost, path)

        visited[current_node] = predecessor 

        for next_node, cost in graph[current_node][1].items():
            if next_node not in visited:
                queue.append((next_node, current_node)) 

    return (count_nodes, float('inf'), [])
