"""
Find if two lists are permutations of each other
for e.g. list 1 = [1, 2, 3] and list 2 = [1, 3, 2] are
permutations of each other
"""
from typing import List


def check_permutations(list_1: List, list_2: List):
    # Check if lengths of both lists are same
    if len(list_1) != len(list_2):
        return False

    # Sort both lists
    list_1.sort()
    list_2.sort()

    # If sorted lists are same, then they are permutations
    if list_1 == list_2:
        return True


def main():
    # list_1 = [1, 2, 3]
    # list_2 = [1, 3, 2]

    list_1 = ['a', 'b', 'c']
    list_2 = ['c', 'a', 'b']

    print(check_permutations(list_1=list_1, list_2=list_2))


if __name__ == "__main__":
    main()

# EOF
