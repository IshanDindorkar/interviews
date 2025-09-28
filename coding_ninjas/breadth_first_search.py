"""
Breadth-first search algorithm
"""


from collections import deque


def bfs(graph, start_node):
    """
    Performs a Breadth-First Search (BFS) on a graph starting from a given node.

    Args:
        graph (dict): The graph represented as an adjacency list.
                      Example: {'A': ['B', 'C'], 'B': ['D'], ...}
        start_node: The starting node for the traversal.

    Returns:
        list: The order in which the nodes were visited.
    """
    # 1. Initialize data structures
    visited = set()
    queue = deque([start_node])
    traversal_order = []

    # Mark the start node as visited
    visited.add(start_node)

    # 2. Loop while the queue is not empty
    while queue:
        # a. Dequeue the current node
        current_node = queue.popleft()

        # b. Process the current node
        traversal_order.append(current_node)

        # c. Explore neighbors
        # Check if the current_node exists in the graph dictionary
        if current_node in graph:
            for neighbor in graph[current_node]:
                # d. Enqueue unvisited neighbors
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    return traversal_order


# --------------------
# Example Usage
# --------------------

# Define an unweighted, undirected graph (represented as an adjacency list)
# Note: For an undirected graph, we must define edges in both directions.
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
result = bfs(graph, start_node)

print(f"Starting Node: {start_node}")
print(f"Graph Traversal Order (BFS): {result}")
# Expected Output: ['A', 'B', 'C', 'D', 'E', 'F']