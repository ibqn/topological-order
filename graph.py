class DAGraph:
    def __init__(self):
        self.nodes = {}

    def _add_edge_ab(self, a, b):
        self.nodes[a].append(b)

    def _add_node(self, a):
        nodes = self.nodes.get(a, [])
        self.nodes[a] = nodes

    def add_edge(self, a, b):
        self._add_node(a)
        self._add_node(b)
        self._add_edge_ab(a, b)

    def __str__(self):
        return f"{self.nodes}"

    def get_nodes(self):
        return self.nodes.keys()

    def get_nodes_at(self, node):
        return self.nodes[node]

    def __len__(self):
        return len(self.nodes)


class TopSort:
    def topsort(self, graph):
        n = len(graph)

        visited = [False] * n

        ordering = []

        for node in graph.get_nodes():
            if not visited[node]:
                self.dfs(node, visited, ordering, graph)

        return ordering

    def dfs(self, node, visited, ordering, graph):
        visited[node] = True

        for edge_node in graph.get_nodes_at(node):
            if not visited[edge_node]:
                self.dfs(edge_node, visited, ordering, graph)

        ordering.insert(0, node)


if __name__ == "__main__":
    graph = DAGraph()

    edges = [
        (0, 1),
        (0, 2),
        (0, 5),
        (1, 3),
        (1, 2),
        (2, 3),
        (2, 4),
        (3, 4),
        (5, 4),
    ]

    for edge in edges:
        graph.add_edge(*edge)

    print(f"graph: {graph}")

    topsort = TopSort()

    print(f"topological order: {topsort.topsort(graph)}")
