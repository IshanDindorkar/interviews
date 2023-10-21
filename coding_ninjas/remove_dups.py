"""
Remove duplicates from list "in place"
Time complexity = O(n)
"""

from typing import List

from loguru import logger


def remove_duplicates(sequence: List):
    i = 0
    for j in range(1, len(sequence)):
        if sequence[j] != sequence[i]:
            i += 1
            sequence[i] = sequence[j]
        logger.debug(f"Pass: {j}: {sequence}")

    return i + 1


def main():
    sequence = input("Enter sequence of numbers, separated by space: \n")
    sequence = [int(num) for num in sequence.split(" ")]
    logger.info(f"Sequence of numbers: {sequence}")

    new_length = remove_duplicates(sequence=sequence)
    logger.info(f"Removed duplicates: {sequence[:new_length]}")


if __name__ == "__main__":
    main()

# EOF
