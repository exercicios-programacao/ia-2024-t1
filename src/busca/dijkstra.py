import heapq

def dijkstra(graph, start: int, goal: int) -> (int, float, [int]):
    distance = {index: float('inf') for index, _ in enumerate(graph)}
    distance[start] = 0
    previous = {}
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == goal:
            path = []
            while current_node in previous:
                path.insert(0, current_node)
                current_node = previous[current_node]
            path.insert(0, start)
            return distance[goal], sum(distance.values()), path

        for neighbor, weight in graph[current_node][1].items():
            new_distance = current_distance + weight
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (new_distance, neighbor))

    return float('inf'), sum(distance.values()), []
