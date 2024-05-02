import networkx as nx
import matplotlib.pyplot as plt
import heapq
import random
import os


class Graph:
    def __init__(self, mode):
        self.graph = {}
        self.mode = mode

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = []
        self.graph[node1].append((node2, weight))

        if node2 not in self.graph:
            self.graph[node2] = []
        self.graph[node2].append((node1, weight))

    def dijkstra(self, source):
        distances = {node: float('inf') for node in self.graph}
        distances[source] = 0
        priority_queue = [(0, source)]
        visited = set()

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    def bellman_ford(self, source):
        distances = {node: float('inf') for node in self.graph}
        distances[source] = 0

        for _ in range(len(self.graph) - 1):
            for node in self.graph:
                for neighbor, weight in self.graph[node]:
                    if distances[node] + weight < distances[neighbor]:
                        distances[neighbor] = distances[node] + weight

        for node in self.graph:
            for neighbor, weight in self.graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    print("Graph contains a negative cycle")
                    return {}

        return distances

    def generate_random_graph(self, num_nodes, num_edges):
        for i in range(1, num_nodes + 1):
            self.graph[i] = []

        edges = []
        for i in range(1, num_nodes + 1):
            for j in range(i + 1, num_nodes + 1):
                edges.append((i, j))

        random.shuffle(edges)

        for edge in edges[:num_edges]:
            self.add_edge(edge[0], edge[1], weight=1)

    def find_shortest_path(self, source, target):
        if self.mode == 1:
            shortest_distances = self.dijkstra(source)
        elif self.mode == 2:
            shortest_distances = self.dijkstra(source)
        shortest_path = []
        current_node = target
        while current_node != source:
            shortest_path.append(current_node)
            neighbors = [(neighbor, weight) for neighbor, weight in self.graph[current_node] if
                         shortest_distances[current_node] == shortest_distances[neighbor] + weight]
            current_node, _ = min(neighbors, key=lambda x: x[1])

        shortest_path.append(source)
        shortest_path.reverse()
        return shortest_path, shortest_distances

    def save_graph(self, source, target):
        G = nx.Graph()
        shortest_path, _ = self.find_shortest_path(source, target)
        for node, neighbors in self.graph.items():
            for neighbor, weight in neighbors:
                G.add_edge(node, neighbor, weight=weight)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800, font_size=12)
        nx.draw_networkx_nodes(self.graph, pos, nodelist=shortest_path, node_color='red', node_size=800)
        if os.path.isfile("res/graph_image.png"):
            os.remove("res/graph_image.png")
        plt.title("Graph Visualization")
        plt.tight_layout()
        plt.savefig("res/graph_image.png", dpi=100)


    def print_shortest_path(self, source, target):
        shortest_path, shortest_distances = self.find_shortest_path(source, target)
        print("Shortest path from node", source, "to node", target, ":", shortest_path)
        print("Shortest distances from node", source, ":")
        for node, distance in shortest_distances.items():
            print("Node:", node, "- Distance:", distance)
