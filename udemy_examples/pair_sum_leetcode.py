"""
Write program to find all pairs of integers
whose sum is equal to given number
"""


def find_pair_with_expected_sum(seq, target):
    traversed_num_dict = {}

    for index, num in enumerate(seq):
        complement = target - num

        if complement in traversed_num_dict.keys():
            return traversed_num_dict[complement], index

        traversed_num_dict[num] = index


def main():
    seq = [2, 6, 3, 9, 11]
    target = 9
    indices = find_pair_with_expected_sum(seq=seq, target=target)
    print(f"The pair is {seq[indices[0]]}, {seq[indices[1]]}")


if __name__ == "__main__":
    main()

# EOF
