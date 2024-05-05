"""Implementação de uma estrutura de grafo."""

def read_graph(filename):
    """Le uma estrutura de grafo de um arquivo e retorna a estrutura."""
    adjacency_list = {}
    with open(filename, encoding="utf-8") as file:
        lines = file.readlines()
        num_vertices = int(lines[0])

        for line in lines[1:num_vertices + 1]:
            parts = line.split()
            if len(parts) == 3:
                index, lat, long = parts
                adjacency_list[int(index)] = {'coordinates': [float(lat), float(long)], 'edges': {}}

        for line in lines[num_vertices + 2:]:
            parts = line.split()
            if len(parts) == 3:
                source, target, distance = parts
                source, target, distance = int(source), int(target), float(distance)
                if source in adjacency_list:
                    adjacency_list[source]['edges'][target] = distance
                if target in adjacency_list:
                    adjacency_list[target]['edges'][source] = distance
    return adjacency_list
