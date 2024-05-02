import os
import sys
import networkx as nx
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox, QLineEdit, QTextEdit
from PyQt5.QtGui import QPixmap
from graph import Graph

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Graph Algorithms")
        self.setGeometry(100, 100, 1000, 600)

        self.graph = None

        self.label_mode = QLabel("Mode:", self)
        self.label_mode.setGeometry(50, 50, 100, 30)
        self.combo_mode = QComboBox(self)
        self.combo_mode.setGeometry(150, 50, 150, 30)
        self.combo_mode.addItem("Dijkstra", 1)
        self.combo_mode.addItem("Bellman-Ford", 2)

        self.label_source = QLabel("Source:", self)
        self.label_source.setGeometry(50, 100, 100, 30)
        self.input_source = QLineEdit(self)
        self.input_source.setGeometry(150, 100, 150, 30)

        self.label_target = QLabel("Target:", self)
        self.label_target.setGeometry(50, 150, 100, 30)
        self.input_target = QLineEdit(self)
        self.input_target.setGeometry(150, 150, 150, 30)

        self.label_num_nodes = QLabel("Number of Nodes:", self)
        self.label_num_nodes.setGeometry(50, 200, 150, 30)
        self.input_num_nodes = QLineEdit(self)
        self.input_num_nodes.setGeometry(200, 200, 100, 30)

        self.label_num_edges = QLabel("Number of Edges:", self)
        self.label_num_edges.setGeometry(50, 250, 150, 30)
        self.input_num_edges = QLineEdit(self)
        self.input_num_edges.setGeometry(200, 250, 100, 30)

        self.button_generate = QPushButton("Generate Random Graph", self)
        self.button_generate.setGeometry(50, 300, 250, 30)
        self.button_generate.clicked.connect(self.generate_random_graph)

        self.button_find_shortest_path_ = QPushButton("Find Shortest Path", self)
        self.button_find_shortest_path_.setGeometry(50, 350, 250, 30)
        self.button_find_shortest_path_.clicked.connect(self.find_shortest_path_)

        self.text_output = QTextEdit(self)
        self.text_output.setGeometry(350, 50, 300, 500)

        self.graph_image_label = QLabel(self)
        self.graph_image_label.setGeometry(700, 50, 300, 500)

    def generate_random_graph(self):
        num_nodes_text = self.input_num_nodes.text()
        num_edges_text = self.input_num_edges.text()

        if not num_nodes_text or not num_edges_text:
            self.text_output.clear()
            self.text_output.append("Please enter both number of nodes and edges.")
            return

        try:
            num_nodes = int(num_nodes_text)
            num_edges = int(num_edges_text)
        except ValueError:
            self.text_output.clear()
            self.text_output.append("Please enter valid numbers for nodes and edges.")
            return

        self.graph = Graph(self.combo_mode.currentData())
        self.graph.generate_random_graph(num_nodes, num_edges)
        self.text_output.clear()
        self.text_output.append("Random graph generated.")
        self.draw_graph(int(self.input_source.text()), int(self.input_target.text()))

    def find_shortest_path_(self):
        if self.graph is None:
            self.text_output.clear()
            self.text_output.append("Generate a graph first.")
            return
        source = int(self.input_source.text())
        target = int(self.input_target.text())
        shortest_path, shortest_distances = self.graph.find_shortest_path(source, target)
        print(source, target)
        self.text_output.clear()
        self.text_output.append(f"Shortest path from node {source} to node {target}: {shortest_path}")
        self.text_output.append("Shortest distances from node {}:".format(source))
        for node, distance in shortest_distances.items():
            self.text_output.append("Node: {} - Distance: {}".format(node, distance))

    def draw_graph(self, source, target):
        self.graph.save_graph(source, target)
        pixmap = QPixmap("res/graph_image.png")
        pixmap_resized = pixmap.scaled(300, 300)
        self.graph_image_label.setPixmap(pixmap_resized)


