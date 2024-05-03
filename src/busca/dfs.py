def dfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em profundidade."""

    stack = [(start, None)]
    visited_nodes = {}
    count_nodes = 0
    
    while stack:
        current_node, predecessor = stack.pop()
        
        if current_node == goal:
            path = [current_node]
            total_cost = 0
                
            while predecessor is not None:
                path.append(predecessor)
                total_cost += graph[predecessor][current_node]['cost']  # Get the cost
                current_node = predecessor
                predecessor = visited_nodes.get(current_node)

            path.reverse()
            return (count_nodes, total_cost, path)

        if current_node not in visited_nodes:
            count_nodes += 1
            visited_nodes[current_node] = predecessor

            for neighbor, edge_cost in graph[current_node].items():
                if neighbor not in visited_nodes:
                    stack.append((neighbor, current_node))
    
    return (count_nodes, float('inf'), [])