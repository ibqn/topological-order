class DGraph:
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


class Cycle:
    def __init__(self, graph):
        self.marked = {}
        self.on_stack = {}
        self.edge_to = {}
        self.cycle = None

        for node in graph.get_nodes():
            if not self.marked.get(node, False) and not self.cycle:
                self._dfs(graph, node)

    def _dfs(self, graph, node_v):
        self.marked[node_v] = True
        self.on_stack[node_v] = True

        for node in graph.get_nodes_at(node_v):
            if self.cycle:
                return

            if not self.marked.get(node, False):
                self.edge_to[node] = node_v
                self._dfs(graph, node)
            elif self.on_stack.get(node, False):
                self.cycle = []
                x = node_v
                while x != node:
                    self.cycle.append(x)
                    x = self.edge_to[x]
                self.cycle.append(node)
                self.cycle.append(node_v)
                print("match", node, self.cycle)

        self.on_stack[node_v] = False

    def has_cycle(self):
        return self.cycle != None


if __name__ == "__main__":
    graph = DGraph()

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

    cycle = Cycle(graph)

    print(f"has {'' if cycle.has_cycle() else 'no '}cycle ")

    files = ["tinyDG.txt", "tinyDAG.txt"]

    for file in files:
        with open(file, "r") as f:
            edges = [e for e in map(lambda l: l.split(), f.readlines()) if len(e) == 2]

        graph = DGraph()

        for edge in edges:
            # print(edge)
            graph.add_edge(*edge)

        cycle = Cycle(graph)

        print(f"has {'' if cycle.has_cycle() else 'no '}cycle ")
