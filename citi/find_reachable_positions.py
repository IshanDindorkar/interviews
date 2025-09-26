def find_reachable_positions(start_square: int,
                             die_sides: int,
                             teleporters: dict[int, int],
                             board_end: int = float('inf')) -> list[int]:
    """
    Calculates the distinct list of positions a player can reach in one turn.

    Args:
        start_square: The player's current position (1-D array index).
        die_sides: The number of sides on the die (D).
        teleporters: A dictionary mapping the 'from' square to the 'to' square.
                     Example: {5: 10, 6: 15} means a teleporter from 5 to 10 and 6 to 15.
        board_end: The last square on the board (inclusive). Defaults to infinity
                   if no board size constraint is specified.

    Returns:
        A sorted list of unique positions the player can potentially jump to.
    """
    reachable_positions = set()

    # 1. Identify all squares that can be reached by a single die roll
    # The possible rolls are 1, 2, ..., die_sides
    die_roll_targets = set()
    for roll in range(1, die_sides + 1):
        target = start_square + roll
        # Optionally, check if the target is within the board limits
        if target <= board_end:
            die_roll_targets.add(target)

    # 2. Check for teleporters and combine destinations

    # Check if the starting square S has a teleporter
    if start_square in teleporters:
        reachable_positions.add(teleporters[start_square])

    # Check each die roll target T for a teleporter
    for target in die_roll_targets:
        if target in teleporters:
            # If a teleporter exists, the final position is the teleporter's destination
            reachable_positions.add(teleporters[target])
        else:
            # If no teleporter, the final position is the square landed on
            reachable_positions.add(target)

    # Remove the starting square from the results if it somehow appeared (shouldn't
    # happen with a positive die roll, but good for robustness).
    if start_square in reachable_positions:
        reachable_positions.remove(start_square)

    # 3. Return a distinct (Set naturally handles this) and sorted list
    return sorted(list(reachable_positions))


# --- Example Usage ---

# Parameters
start_square = 5
die_sides = 3
teleporters = {
    5: 10,  # From Start: (5 -> 10)
    6: 15,  # From Die Roll 1: (6 -> 15)
    7: 20,  # From Die Roll 2: (7 -> 20)
    8: 8,  # A teleporter that doesn't move you (8 -> 8). If used, 8 is the final pos.
    10: 1  # This teleporter is NOT used because 10 is a destination in this turn, not a landing square
}
board_end = 25  # Assuming the board ends at square 25

# Call the function
distinct_positions = find_reachable_positions(start_square, die_sides, teleporters, board_end)

print(f"Start Square: {start_square}")
print(f"Die Sides: {die_sides}")
print(f"Die Roll Targets (before teleporters): {sorted(list({5 + r for r in range(1, die_sides + 1)}))}")
print(f"Teleporters: {teleporters}")
print("-" * 30)
print(f"Distinct Reachable Positions: {distinct_positions}")
# Expected: [8, 10, 15, 20].
# Roll 1 (6) -> Teleporter (6:15) -> 15
# Roll 2 (7) -> Teleporter (7:20) -> 20
# Roll 3 (8) -> Teleporter (8:8) -> 8
# Start (5) -> Teleporter (5:10) -> 10