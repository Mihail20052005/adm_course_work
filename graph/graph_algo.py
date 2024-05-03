import heapq
from graph import graph_structure


def dijkstra(graph_, source: int):

    distances = {node: float('inf') for node in graph_}
    distances[source] = 0
    priority_queue = [(0, source)]
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graph_[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def bellman_ford(graph_, source: int):
    distances = {node: float('inf') for node in graph_}
    distances[source] = 0

    for _ in range(len(graph_) - 1):
        for node in graph_:
            for neighbor, weight in graph_[node]:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    for node in graph_:
        for neighbor, weight in graph_[node]:
            if distances[node] + weight < distances[neighbor]:
                print("Graph contains a negative cycle")
                return {}

    return distances


def find_shortest_path(graph_, mode, source: int, target: int):
    if mode == 1:
        shortest_distances = dijkstra(graph_, source)
    elif mode == 2:
        shortest_distances = bellman_ford(graph_, source)
    shortest_path = []
    current_node = target
    while current_node != source:
        shortest_path.append(current_node)
        neighbors = [(neighbor, weight) for neighbor, weight in graph_[current_node] if
                     shortest_distances[current_node] == shortest_distances[neighbor] + weight]
        current_node, _ = min(neighbors, key=lambda x: x[1])

    shortest_path.append(source)
    shortest_path.reverse()
    return shortest_path, shortest_distances


def print_shortest_path(graph_, mode,  source: int, target: int):
    shortest_path, shortest_distances = find_shortest_path(graph_, mode,  source, target)
    print("Shortest path from node", source, "to node", target, ":", shortest_path)
    print("Shortest distances from node", source, ":")
    for node, distance in shortest_distances.items():
        print("Node:", node, "- Distance:", distance)

