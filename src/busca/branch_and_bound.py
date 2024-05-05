import heapq

def branch_and_bound(graph, start, goal):
    queue = [(0, start, [start])]
    distance = {index: float('inf') for index, _ in enumerate(graph)}

    while queue:
        current_distance, current_node, path = heapq.heappop(queue)

        if current_node == goal:
            return len(path), current_distance, path

        for neighbor, weight in graph[current_node][1].items():
            new_distance = current_distance + weight
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor, path + [neighbor]))

    return float('inf'), None, []