"""
Bellman-Ford Algorithm: Find the shortest path between vertices of Graph having negative edge weights
"""

from interviews.custom_exceptions.negative_weight_cycle import NegativeWeightCycle


class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._graph_elems = []

    @property
    def vertices(self):
        return self._vertices

    def add_edge(self, first_vertex: int, second_vertex: int, edge_weight: int):
        self._graph_elems.append((first_vertex, second_vertex, edge_weight))

    def bellman_ford(self, start_vertex):
        distances = [float("infinity")] * self._vertices
        distances[start_vertex] = 0

        for _ in range(self._vertices - 1):
            for first_vertex, second_vertex, edge_weight in self._graph_elems:
                if (distances[first_vertex] != float("infinity") and
                        distances[first_vertex] + edge_weight < distances[second_vertex]):
                    distances[second_vertex] = distances[first_vertex] + edge_weight

        # Detect negative weight cycles
        for first_vertex, second_vertex, edge_weight in self._graph_elems:
            if (distances[first_vertex] != float("infinity") and
                    distances[first_vertex] + edge_weight < distances[second_vertex]):
                raise NegativeWeightCycle()

                return

        return distances


def main():
    graph = Graph(vertices=5)
    graph.add_edge(0, 1, -1)
    graph.add_edge(0, 2, 4)
    graph.add_edge(1, 2, 3)
    graph.add_edge(1, 3, 2)
    graph.add_edge(1, 4, 2)
    graph.add_edge(3, 2, 5)
    graph.add_edge(3, 1, 1)
    graph.add_edge(4, 3, -3)

    print(graph.bellman_ford(start_vertex=0))


if __name__ == "__main__":
    main()

# EOF

