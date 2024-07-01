def dfs(graph, start, goal):
    if start not in graph or goal not in graph:
        raise Exception('Vértice não encontrado no grafo')
    cost = 0
    path = []
    visited = []
    backtracking_list = []
    s = []
    current_node = (-1, -1)
    s.append((start, -1))
    while len(s) > 0:
        v = s.pop()
        if goal == v[0]:
            path.append(v[0])
            current_node = v
            backtracking_list.append(current_node)

            while current_node[1] != -1:
                for node in backtracking_list:
                    if node[0] == current_node[1]:
                        cost += graph[current_node[0]][1][current_node[1]]
                        current_node = node
                        path.insert(0, current_node[0])
                        break

            return (len(visited), cost, path)
        
        if v[0] not in visited:
            visited.append(v[0])
            backtracking_list.append(v)
            for u in graph[v[0]][1].keys():
                if u not in visited:
                    s.append((u, v[0]))