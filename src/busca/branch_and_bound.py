from graph import get_neighbors

def branch_and_bound(graph, start: int, goal: int) -> (int, float, [int]):
    visited = set() # Uma lista contendo os nodos já visitados.
    stack = [(0, 0, [start])]  # (lower_bound, cost, path).
    best = []

    while stack:
        stack.sort()  # Ordena a pilha com base no lower_bound.
        lb, cost, current_path = stack.pop(0) # Atribui os valores inicias e remove o primeiro elemento da stack.
        node = current_path[-1] # Atribui a "node" o valor do último elemento no path da lista.

        if node == goal: # Testa se o nodo é o goal.
            if not best: # Testa se o novo caminho é menos custoso que o já encontrado.
                best.append((len(visited), cost, current_path)) # Atribui o caminho recém encontrado como o melhor.
            elif best and best[0][1] > cost:
                best[0] = (len(visited), cost, current_path)

        if node not in visited:
            visited.add(node)
            neighbors = get_neighbors(graph, node)
            for neighbor, edge_cost in neighbors:
                if neighbor not in visited:
                    if not best or (best and cost + edge_cost < best[0][1]):
                        new_cost = cost + edge_cost
                        new_path = current_path + [neighbor]
                        new_lb = new_cost  # No Branch and Bound puro, não usamos heurística
                        stack.append((new_lb, new_cost, new_path))

    return best or "Nenhum caminho foi encontrado!"
