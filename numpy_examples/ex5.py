"""
Create random array using Numpy with and without Normal Distribution
"""

import numpy as np


def main():
    # Generate sequence within range
    arr = np.arange(1, 5, 3)  # [1, 4]
    arr = np.arange(1, 10, 3)  # [1, 4, 7]
    arr = np.arange(1, 10)  # [1 2 3 4 5 6 7 8 9]
    print(arr)
    print("####################")

    # Generate numbers from random distribution
    arr = np.random.rand(2, 3)
    print("Random numbers")
    print(arr)
    print("####################")

    # Generate numbers from Normal Distribution
    arr = np.random.randn(2, 3)
    print("Standard Normal Distribution")
    print(arr)
    print("####################")

    # Generate an empty Numpy array with junk values
    empty_array = np.empty((3, 3))
    print(empty_array)
    print("####################")

    # Generate Numpy array and fill it with given value
    # np.full is generalized form of np.zeros and np.ones
    arr = np.full(shape=(3, 3), fill_value=3)
    print(arr)
    print("####################")

    ones = np.full(shape=(3, 3), fill_value=1)
    print(ones)
    print("####################")


if __name__ == "__main__":
    main()

# EOF
