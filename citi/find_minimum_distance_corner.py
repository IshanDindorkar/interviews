import collections
from typing import List, Tuple, Optional


def find_min_distance_corner(grid: List[List[int]],
                             start_coords: Tuple[int, int]) -> Optional[Tuple[int, int]]:
    """
    Finds the coordinates of the closest reachable passable corner cell
    from a given starting cell in a grid using Breadth-First Search (BFS).

    The four corners of the grid are (0, 0), (0, C-1), (R-1, 0), and (R-1, C-1).
    The starting cell itself is excluded from the list of potential destinations.

    Args:
        grid: A 2D list of integers where 0 is passable and 1 is blocked.
        start_coords: A tuple (row, col) representing the starting position.

    Returns:
        The coordinates (row, col) of the closest passable corner, or None
        if no other passable corner is reachable.
    """
    R = len(grid)
    if R == 0:
        return None
    C = len(grid[0])
    if C == 0:
        return None

    start_r, start_c = start_coords

    # 1. Identify all four corner coordinates
    all_corners = {
        (0, 0),
        (0, C - 1),
        (R - 1, 0),
        (R - 1, C - 1)
    }

    # 2. Determine the set of valid destination corner cells
    # Destinations must be:
    # a) Corners (excluding the start cell)
    # b) Passable (grid value 0)
    target_corners = set()
    for r, c in all_corners:
        # Check if the coordinates are within bounds and the cell is passable
        if 0 <= r < R and 0 <= c < C and grid[r][c] == 0:
            if (r, c) != start_coords:
                target_corners.add((r, c))

    # Initial check: Is the starting cell valid?
    if not (0 <= start_r < R and 0 <= start_c < C) or grid[start_r][start_c] == 1:
        print(f"Error: Starting cell {start_coords} is invalid or blocked.")
        return None

    if not target_corners:
        print("No other passable corner cells exist to reach.")
        return None

    print(f"Grid Size: {R}x{C}")
    print(f"Start: {start_coords}")
    print(f"Passable Targets: {target_corners}")

    # Initialize BFS
    # Queue stores: ((row, col), distance)
    queue = collections.deque([(start_coords, 0)])
    visited = {start_coords}

    # Directions: (dr, dc) for Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        (r, c), dist = queue.popleft()

        # Check if the current cell is a target corner
        if (r, c) in target_corners:
            print(f"Found closest corner: {r, c} at distance {dist}")
            return (r, c)

        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Boundary and Passability check
            if (R > nr >= 0 == grid[nr][nc] and
                    0 <= nc < C and
                    (nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append(((nr, nc), dist + 1))

    # If the queue empties without finding a target
    print("No passable corner cells are reachable from the starting cell.")
    return None


# --- Configuration and Execution ---

# ASSUMPTION: Define a sample 5x5 grid (0=passable, 1=blocked)
SAMPLE_GRID = [
    [0, 0, 0, 0, 1],  # (0, 4) is blocked
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]  # (4, 0) and (4, 4) are passable
]

# ASSUMPTION: Define the starting cell (must be passable)
START_CELL = (0, 0)

# Run the algorithm
result_coords = find_min_distance_corner(SAMPLE_GRID, START_CELL)

# Output the result
if result_coords:
    r, c = result_coords
    print(f"\nFinal Result: The closest reachable passable corner is at coordinates {r, c}.")
else:
    print("\nFinal Result: -1 (Not possible to reach any other passable corner).")

# --- Example 2: No Path Possible ---
print("\n" + "=" * 50 + "\n")
SAMPLE_GRID_2 = [
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0]
]
START_CELL_2 = (0, 0)

result_coords_2 = find_min_distance_corner(SAMPLE_GRID_2, START_CELL_2)
if result_coords_2:
    r, c = result_coords_2
    print(f"\nFinal Result: The closest reachable passable corner is at coordinates {r, c}.")
else:
    # Per user request: return -1 if not possible
    print("\nFinal Result: -1 (Not possible to reach any other passable corner).")