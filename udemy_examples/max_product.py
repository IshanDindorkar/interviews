"""
Find max product of two integers in an array of all
positive numbers
"""
import numpy as np


def find_max_product(seq):
    seq.sort(reverse=True)
    return seq[0] * seq[1]


def main():
    seq = [7, 8, 1, 2, 4]
    print(find_max_product(seq=seq))


if __name__ == "__main__":
    main()

# EOF

