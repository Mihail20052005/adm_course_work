from graph import *
if __name__ == "__main__":
    print("Choose: 1. Create graph mode,  2. Generate random graph")
    n = int(input())
    print("Choose: 1. Dijkstra algorithm, 2. Dynamic programming (Bellmann Ford algo)")
    m = int(input())
    graph = Graph(mode=m)
    if n == 2:
        print("Write num_nodes, num_edges, source_node, target_node")
        num_nodes, num_edges, source_node, target_node = map(int, input().split())
        graph.generate_random_graph(num_nodes, num_edges)
        graph.print_shortest_path(source_node, target_node)
        graph.draw_graph(source_node, target_node)
    else:
        print("Write start node, end node, weight; for exit - write 0 0 0")
        while True:
            start_node, end_node, weight = map(int, input().split())
            if start_node == 0:
                break
            else:
                graph.add_edge(start_node, end_node, weight)
        print("Write source_node,target_node")
        source_node, target_node = map(int, input().split())
        graph.print_shortest_path(source_node, target_node)
        graph.draw_graph(source_node, target_node)

