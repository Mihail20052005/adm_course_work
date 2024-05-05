import unittest
from graph.graph_algo import dijkstra, bellman_ford, find_shortest_path
from graph.graph_structure import Graph
from gui.gui import MainWindow, SecondWindow
from PyQt5.QtWidgets import QApplication


class TestGraphAlgorithms(unittest.TestCase):

    def setUp(self):
        self.graph = {
            1: [(2, 5), (3, 2)],
            2: [(1, 5), (3, 1), (4, 6)],
            3: [(1, 2), (2, 1), (4, 3)],
            4: [(2, 6), (3, 3)]
        }

    def test_dijkstra(self):
        distances = dijkstra(self.graph, 1)
        self.assertEqual(distances, {1: 0, 2: 3, 3: 2, 4: 5})

    def test_bellman_ford(self):
        distances = bellman_ford(self.graph, 1)
        self.assertEqual(distances, {1: 0, 2: 3, 3: 2, 4: 5})

    def test_find_shortest_path(self):
        shortest_path, shortest_distances = find_shortest_path(self.graph, 1, 1, 4)
        self.assertEqual(shortest_path, [1, 3, 4])
        self.assertEqual(shortest_distances, {1: 0, 2: 3, 3: 2, 4: 5})


class TestGraphStructure(unittest.TestCase):

    def setUp(self):
        self.graph = Graph(1)

    def test_add_edge(self):
        self.graph.add_edge(1, 2, 5)
        self.assertEqual(self.graph.graph, {1: [(2, 5)], 2: [(1, 5)]})

    def test_generate_random_graph(self):
        self.graph.generate_random_graph(5, 7)
        self.assertEqual(len(self.graph.graph), 5)  # Проверяем количество узлов
        num_edges = sum(len(edges) for edges in self.graph.graph.values())  # Общее количество рёбер
        self.assertEqual(num_edges, 14)  # Проверяем количество рёбер




# class TestGUI(unittest.TestCase):
#
#     def setUp(self):
#         self.app = QApplication([])
#
#     def test_main_window(self):
#         main_window = MainWindow()
#         main_window.combo_mode.setCurrentIndex(0)
#         main_window.input_source.setText("1")
#         main_window.input_target.setText("5")
#         main_window.input_num_nodes.setText("10")
#         main_window.input_num_edges.setText("20")
#         main_window.generate_random_graph()
#         main_window.find_shortest_path_()
#         self.assertIsNotNone(main_window.graph)
#
#     def tearDown(self):
#         self.app.quit()


if __name__ == '__main__':
    unittest.main()