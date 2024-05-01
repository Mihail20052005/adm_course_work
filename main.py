from graph import *
if __name__ == "__main__":
    print("Введите режим: 1. Режим создания графа 2. Генерация случайного графа")
    n = int(input())
    if n == 2:
        print("Введите num_nodes, num_edges, source_node, target_node")
        graph = Graph()
        num_nodes, num_edges, source_node, target_node = map(int, input().split())
        graph.generate_random_graph(num_nodes, num_edges)
        graph.print_shortest_path(source_node, target_node)
        graph.draw_graph(source_node, target_node)