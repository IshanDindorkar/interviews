"""
Merge sort implementation
"""
from typing import List

from loguru import logger


def merge_sort(sequence: List):
    if len(sequence) > 1:
        # Split sequence of numbers into two halves
        middle_pos_index = len(sequence) // 2  # this will give integer part of division ("floor" division)
        left_half = sequence[:middle_pos_index]
        right_half = sequence[middle_pos_index:]

        # Recursive calls to merge_sort function using left and right halves of sequence
        merge_sort(left_half)
        merge_sort(right_half)

        # Initializing counters
        i = j = k = 0

        # Element-to-element comparison between left and right halves of sequence
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                sequence[k] = left_half[i]
                i += 1
            else:
                sequence[k] = right_half[j]
                j += 1
            k += 1

        # Fill up remaining elements from left and right halves
        while i < len(left_half):
            sequence[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            sequence[k] = right_half[j]
            j += 1
            k += 1


def main():
    sequence = input("Enter numbers to be sorted, separated by comma: \n")
    sequence = [int(num) for num in sequence.split(",")]
    logger.info(f"Unsorted sequence of numbers: {sequence}")

    merge_sort(sequence=sequence)
    logger.info(f"Sorted sequence of numbers: {sequence}")


if __name__ == "__main__":
    main()

# EOF
