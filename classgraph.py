class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []

        if v not in self.adj_list:
            self.adj_list[v] = []

        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        result = []

        while queue:
            node = queue.pop(0)
            result.append(node)

            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print("Graph BFS:", " -> ".join(result))

    def dfs(self, start):
        visited = set()
        result = []

        def dfs_helper(node):
            visited.add(node)
            result.append(node)

            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start)
        print("Graph DFS:", " -> ".join(result))


if __name__ == "__main__":
    graph = Graph()

    graph.add_edge("G", "E")
    graph.add_edge("G", "N")
    graph.add_edge("E", "I")
    graph.add_edge("E", "L")
    graph.add_edge("N", "L")
    graph.add_edge("N", "A")
    graph.add_edge("I", "A")

    graph.bfs("G")
    graph.dfs("G")