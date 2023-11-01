"""
Basic example of sorting list of tuples in-place
"""


def main():
    seqs = [(1, 0), (4, 2), (7, 9), (2, 5)]
    seqs.sort(key=lambda x: x[0])
    print(seqs)


if __name__ == "__main__":
    main()

# EOF
