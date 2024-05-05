"""Implementação de uma estrutura de grafo."""


def read_graph(filename):
    """Le uma estrutura de grafo de um arquivo e retorna a estrutura."""
    lista = {}
    with open(filename, encoding="utf-8") as file:
        lines = file.readlines()
        num_vertices = int(lines[0])

        for line in lines[1:num_vertices + 1]:
            parts = line.split()
            if len(parts) == 3:
                index, lat, long = parts
                lista[int(index)] = {'coordinates':
                                     [float(lat), float(long)], 'edges': {}}

        for line in lines[num_vertices + 2:]:
            parts = line.split()
            if len(parts) == 3:
                start, goal, distance = parts
                start, goal, distance = int(start), int(start), float(distance)
                if start in lista:
                    lista[start]['edges'][goal] = distance
                if goal in lista:
                    lista[goal]['edges'][start] = distance
    return lista
