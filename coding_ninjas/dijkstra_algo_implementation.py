"""
Dijkstra Implementation:
Find the shortest path from given point to all other points in the Graph.
It is useful only in graphs with non-negative weights.
Otherwise, checkout Bellman-Ford algorithm

There are 2 data structures being used
1. Dictionary: Create "graph" and "distances"
2. Priority Queue: Track distances from start vertex to all other vertices in the Graph

Dijkstra's algorithm has a time complexity:
1. O(V^2) for dense graphs when using an adjacency matrix
2. O((V + E) * log(V)) when using a priority queue for sparse graphs,
where V is the number of vertices and E is the number of edges.
"""

import heapq
from typing import Dict


def dijkstra(graph: Dict, start_vertex: str):
    # Step 1: Create dictionary to store distances from start vertex to all other vertices in the graph
    # Initialize all distances to "infinity"
    distances = {vertex: float("infinity") for vertex in graph.keys()}
    distances[start_vertex] = 0

    # Step 2: Push start vertex with distance 0
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue  # we already got the shortest path between start_vertex and current_vertex so continue with others

        # Step 3: Iterate over all neighbors of current vertex
        for neighbor, weight in graph[current_vertex].items():  # iterate over all neighbors of current vertex
            new_distance = current_distance + weight

            # If distance between neighbor to start vertex thru current vertex is less than current distance, update it
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances


def main():
    # Create a Graph representing travel itinerary
    salesman_graph = dict()
    salesman_graph["A"] = {
        "B": 1,
        "C": 4
    }
    salesman_graph["B"] = {
        "C": 2,
        "D": 5
    }
    salesman_graph["C"] = {
        "D": 1
    }
    salesman_graph["D"] = {
        "E": 3
    }
    salesman_graph["E"] = {}

    start_vertex = input("Enter starting point (A-E): \n")
    distances = dijkstra(graph=salesman_graph, start_vertex=start_vertex)
    print(distances)   # {'A': 0, 'B': 1, 'C': 3, 'D': 4, 'E': 7}


if __name__ == "__main__":
    main()

# EOF
