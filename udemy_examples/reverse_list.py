"""
Reverse given list of numbers
"""

from typing import List


def reverse_list(seq: List):
    for index in range(int(len(seq) / 2)):
        swapping_index = len(seq) - index - 1
        temp = seq[index]
        seq[index] = seq[swapping_index]
        seq[swapping_index] = temp

    return seq


def main():
    seq = input("Enter sequence of numbers, separated by space: \n")
    seq = [int(item) for item in seq.split(" ")]
    print(f"The original list: \n{seq}")
    print(f"The reversed list: \n{reverse_list(seq=seq)}")


if __name__ == "__main__":
    main()

# EOF
