import array
import time

import numpy as np


def create_arr_array_mod():
    # Creation of array
    arr = array.array("i", [1, 2, 3, 4])  # Time & Space complexity = O(N)
    print(arr)

    # Insertion of an element into array at the beginning
    # Time complexity = O(N) (worst case as we have to shift all elements)
    # Space complexity = O(1)
    arr.insert(0, 6)
    print(arr)

    # Insertion of an element into middle of the array
    arr.insert(2, 8)
    print(arr)

    # Insertion of an element at the end of array
    # Time complexity = O(1) (best case as we do not have to shift any element)
    # Space complexity = O(1)
    arr.insert(len(arr), 15)
    print(arr)


def create_arr_numpy_mod():
    # Creation of array
    arr1 = np.array([1, 2, 3, 4], dtype=int)
    print(arr1)

    # Insertion of element into an array
    arr1 = np.insert(arr=arr1, obj=3, values=[5, 6], axis=0)
    print(arr1)

    arr2 = np.array([[1, 2], [3, 4]])
    arr2 = np.insert(arr=arr2, obj=1, values=[5, 6], axis=0)
    print(arr2)

    arr2 = np.array([[1, 2], [3, 4]])
    arr2 = np.insert(arr=arr2, obj=1, values=[5, 6], axis=1)
    print(arr2)

    arr3 = np.array([[1, 2, 3],
                    [4, 5, 6]])
    print(arr3)
    print(arr3.shape)





def main():
    # create_arr_array_mod()
    create_arr_numpy_mod()



if __name__ == "__main__":
    main()

# EOF
