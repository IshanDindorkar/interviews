"""
Merge overlapping intervals
Time complexity = O(n log n)
"""

from typing import List

from loguru import logger


def merge_overlapping_intervals(intervals: List):
    merged_overlapped_intervals = []

    # Sort intervals
    intervals.sort(key=lambda x: x[0])
    logger.info(f"Sorted intervals: {intervals}")

    # Merge intervals if overlapping
    for interval in intervals:
        if (len(merged_overlapped_intervals) == 0 or
                merged_overlapped_intervals[-1][1] < interval[0]):
            merged_overlapped_intervals.append(interval)
        else:
            merged_interval = (merged_overlapped_intervals[-1][0],
                               max(merged_overlapped_intervals[-1][1], interval[1]))
            merged_overlapped_intervals[-1] = merged_interval

    return merged_overlapped_intervals


def main():
    interval_1 = (4, 5)
    interval_2 = (5.15, 6)
    interval_3 = (5.45, 7)  # this overlaps with interval_2
    interval_4 = (7.15, 8)

    intervals = [interval_2, interval_1, interval_4, interval_3]
    logger.info(f"Merged overlapping intervals: {merge_overlapping_intervals(intervals=intervals)}")


if __name__ == "__main__":
    main()

# EOF
