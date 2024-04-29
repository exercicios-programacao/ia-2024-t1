import sys

def read_graph(filename: str):
    graph = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
    
        num_vertices = int(lines[0])
        num_edges = int(lines[num_vertices + 1])

        for line in lines[1:num_vertices + 1]:
            parts = line.split()
            if len(parts) == 3:
                index, lat, long = parts
                graph[int(index)] = [[float(lat), float(long)], {}]

        for line in lines[num_vertices + 2:]:
            parts = line.split()
            if len(parts) == 3:
                source, target, distance = parts
                source, target, distance = int(source), int(target), float(distance)
                if source in graph:
                    graph[source][1][target] = distance
    return graph