"""
Bubble sort implementation
"""

import time
from typing import List
from loguru import logger


def bubble_sort(sequence: List):
    len_of_seq = len(sequence)
    logger.debug(f"Count of numbers in the sequence: {len_of_seq}")

    swapped = False

    for out_ind in range(len_of_seq - 1):  # outer loop
        for in_ind in range(0, len_of_seq - out_ind - 1):  # inner loop; excluding last "out_ind" elements
            if sequence[in_ind] > sequence[in_ind + 1]:
                sequence[in_ind], sequence[in_ind + 1] = sequence[in_ind + 1], sequence[in_ind]
                swapped = True

        if not swapped:
            break   # the list of numbers is already sorted so breaking the outer loop

    return sequence


def main():
    unsorted_sequence = input("Enter numbers to be sorted separated by comma: \n")
    unsorted_sequence = unsorted_sequence.split(",")
    unsorted_sequence = [int(num) for num in unsorted_sequence]
    logger.info(f"Unsorted sequence of numbers: {unsorted_sequence}")

    start_time = time.time()
    sorted_sequence = bubble_sort(unsorted_sequence)
    end_time = time.time()
    logger.info(f"Sorted sequence of numbers: {sorted_sequence}")
    logger.debug(f"Time it took: {end_time - start_time} secs")


if __name__ == "__main__":
    main()

# EOF
