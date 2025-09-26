def find_passable_indices(grid):
    """
    Finds the row and column indices that are completely passable ('0's).

    Args:
        grid: A list of lists (the 2-D grid) consisting of '0' and '+'.

    Returns:
        A tuple containing two lists: (passable_row_indices, passable_col_indices).
    """
    if not grid:
        return [], []

    num_rows = len(grid)
    num_cols = len(grid[0])

    passable_rows = []
    passable_cols = []

    # 1. Find Completely Passable Rows
    for i in range(num_rows):
        # A row is passable if the character '+' is NOT in it.
        if '+' not in grid[i]:
            passable_rows.append(i)

    # 2. Find Completely Passable Columns
    # We iterate through each column index (j)
    for j in range(num_cols):
        is_passable = True
        # Check every cell in that column (i)
        for i in range(num_rows):
            if grid[i][j] == '+':
                # Found an impassable cell, so the column is not passable
                is_passable = False
                break

        if is_passable:
            passable_cols.append(j)

    return passable_rows, passable_cols


# --- Example Usage ---

grid_example = [
    ['0', '+', '0', '0'],
    ['0', '0', '0', '0'],
    ['+', '0', '+', '0'],
    ['0', '0', '0', '0']
]

rows, cols = find_passable_indices(grid_example)

print(f"Grid:")
for row in grid_example:
    print(row)

print("\nCompletely Passable Row Indices:", rows)
print("Completely Passable Column Indices:", cols)