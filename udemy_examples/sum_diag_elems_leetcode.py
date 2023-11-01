"""
Find sum of all diagonal elements in 2D array
Time complexity = O(n)
Space complexity = O(1)
"""
import numpy
import numpy as np


def sum_diag_elems(arr: numpy.array):
    total = 0

    for index in range(arr.shape[0]):
        total += arr[index][index]

    return total


def main():
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"The input array: \n{arr}")
    print(f"Sum of diagonal elements: \n{sum_diag_elems(arr=arr)}")


if __name__ == "__main__":
    main()

# EOF
