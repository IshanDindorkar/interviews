"""
Delete column and replace with a new column
in array
"""


import numpy as np


def main():
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(arr)

    new_arr = np.delete(arr, 1, axis=1)
    print(new_arr)

    new_column = np.array([[10, 10, 10]])
    new_arr = np.insert(new_arr, 1, new_column, axis=1)
    print(new_arr)


if __name__ == "__main__":
    main()

# EOF

