def branch_and_bound(graph, start, goal):
    best_path = [] 
    best_path_length = float('inf') 

    def backtrack(curr_node, curr_path, curr_length):
        nonlocal best_path, best_path_length

        if curr_length >= best_path_length:
            return

        if curr_node == goal:  
            best_path = curr_path[:]  
            best_path_length = curr_length  
            return

        neighbors = graph.neighbors(curr_node)
        for neighbor in neighbors:
            if neighbor not in curr_path:  
                new_length = curr_length + graph.distance(curr_node, neighbor)
                backtrack(neighbor, curr_path + [neighbor], new_length)

    backtrack(start, [start], 0)
    return best_path_length, best_path
