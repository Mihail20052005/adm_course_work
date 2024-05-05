import networkx as nx
import matplotlib.pyplot as plt
import heapq
import random
import os

from graph import graph_algo


class Graph:
    def __init__(self, mode):
        """
        Класс Graph представляет собой объект для работы с графами.

        Args:
        mode (str): Режим работы с графом. Может быть "Dijkstra" для алгоритма Дейкстры или "BellmanFord" для алгоритма Беллмана-Форда.
        """
        self.graph = {}
        self.mode = mode

    def graph_(self):
        """
        Возвращает словарь, представляющий граф.

        Returns:
        dict: Словарь, представляющий граф, где ключи - это узлы, а значения - список смежных узлов с их весами.
        """
        return self.graph

    def add_edge(self, node1, node2, weight):
        """
        Добавляет ребро между двумя узлами в граф.

        Args:
        node1: Первый узел.
        node2: Второй узел.
        weight: Вес ребра между узлами.
        """
        if node1 not in self.graph:
            self.graph[node1] = []
        self.graph[node1].append((node2, weight))

        if node2 not in self.graph:
            self.graph[node2] = []
        self.graph[node2].append((node1, weight))

    def generate_random_graph(self, num_nodes, num_edges):
        """
        Генерирует случайный граф с указанным количеством узлов и рёбер.

        Args:
        num_nodes: Количество узлов в графе.
        num_edges: Количество рёбер в графе.
        """
        for i in range(1, num_nodes + 1):
            self.graph[i] = []

        edges = []
        for i in range(1, num_nodes + 1):
            for j in range(i + 1, num_nodes + 1):
                edges.append((i, j))

        random.shuffle(edges)

        for edge in edges[:num_edges]:
            self.add_edge(edge[0], edge[1], weight=1)

    def save_graph(self, source, target):
        """
        Визуализирует граф и сохраняет изображение с выделенным кратчайшим путём между заданными узлами.

        Args:
        source: Исходный узел для поиска кратчайшего пути.
        target: Целевой узел для поиска кратчайшего пути.
        """
        G = nx.Graph()
        shortest_path, _ = graph_algo.find_shortest_path(self.graph, self.mode,  source, target)
        for node, neighbors in self.graph.items():
            for neighbor, weight in neighbors:
                G.add_edge(node, neighbor, weight=weight)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800, font_size=12)
        nx.draw_networkx_nodes(self.graph, pos, nodelist=shortest_path, node_color='red', node_size=800)
        plt.title("Визуализация графа")
        plt.tight_layout()
        plt.savefig("res/graph_image_new.png", dpi=100)
