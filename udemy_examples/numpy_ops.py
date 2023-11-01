"""
Numpy operations: Insertion and Addition
Notes:
1. When inserting or deleting a row/column, axis = 0 means adding / deleting row
while axis = 1 means adding / deleting new column
2. In aggregating operations like adding numbers, axis = 0 means add
numbers column wise while axis = 1 means adding numbers row wise

"""

import numpy as np


def main():
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"Original array: \n{arr}")

    print(f"Addition of numbers column wise: \n{arr.sum(axis=0)}")
    print(f"Addition of numbers row wise: \n{arr.sum(axis=1)}")

    # Adding new array "padding" as a row in numpy array
    padding = np.array([0, 0, 0])
    new_arr = np.insert(arr, obj=0, values=padding, axis=0)
    print(f"New array after addition of row: \n{new_arr}")

    # Adding new array "padding" as a column in numpy array
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    padding = np.array([0, 0, 0])
    new_arr = np.insert(arr, obj=0, values=padding, axis=1)
    print(f"New array after addition of column: \n{new_arr}")


if __name__ == "__main__":
    main()

# EOF
