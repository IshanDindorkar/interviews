"""
Binary search implementation
"""
from typing import List

from loguru import logger


def binary_search(sequence: List, target_num: int):
    low = 0
    high = len(sequence) - 1

    while low <= high:
        middle_pos_ind = (low + high) // 2
        if target_num == sequence[middle_pos_ind]:
            return middle_pos_ind
        elif target_num > sequence[middle_pos_ind]:
            low = middle_pos_ind + 1
        else:
            high = middle_pos_ind - 1

    return -1


def main():
    sequence = input("Enter sequence of numbers, separated by space: \n")
    sequence = [int(num) for num in sequence.split(" ")]
    logger.info(f"Sequence of numbers: {sequence}")
    sequence.sort()
    logger.info(f"Sorted list of numbers: {sequence}")

    target_num = int(input("Enter number to be searched in the sequence: \n"))
    logger.info(f"Number to be searched: {target_num}")

    index = binary_search(sequence=sequence,
                          target_num=target_num)
    logger.info(f"Target number is at index: {index}")


if __name__ == "__main__":
    main()

# EOF
