import networkx as nx
import matplotlib.pyplot as plt
import heapq
import random

class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, node1, node2, weight):
        self.graph.add_edge(node1, node2, weight=weight)

    def dijkstra(self, source):
        distances = {node: float('inf') for node in self.graph.nodes()}
        distances[source] = 0
        priority_queue = [(0, source)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, attr in self.graph[current_node].items():
                distance = current_distance + attr['weight']
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    def generate_random_graph(self, num_nodes, num_edges):
        for i in range(1, num_nodes + 1):
            self.graph.add_node(i)

        edges = []
        for i in range(1, num_nodes + 1):
            for j in range(i + 1, num_nodes + 1):
                edges.append((i, j))

        random.shuffle(edges)

        for edge in edges[:num_edges]:
            self.add_edge(edge[0], edge[1], weight=1)

    def draw_graph(self, source, target):
        shortest_distances = self.dijkstra(source)
        shortest_path = nx.shortest_path(self.graph, source=source, target=target, weight='weight')

        pos = nx.spring_layout(self.graph)  # positions for all nodes
        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=800, font_size=12)

        edge_labels = {(u, v): d['weight'] for u, v, d in self.graph.edges(data=True)}
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        nx.draw_networkx_nodes(self.graph, pos, nodelist=shortest_path, node_color='red', node_size=800)
        nx.draw_networkx_edges(self.graph, pos, edgelist=[(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)], edge_color='red', width=2)

        plt.title("Graph with Shortest Path")
        plt.show()

        print("Shortest path from node", source, "to node", target, ":", shortest_path)

