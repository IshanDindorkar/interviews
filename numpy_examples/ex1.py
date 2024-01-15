"""
Vector operations on Numpy arrays
"""


import numpy as np

arr1 = np.array([7, 8, 9, 10])
arr2 = np.array([1, 2, 3, 4])
arr3 = arr1 + arr2
print(arr3)

arr3 = arr3 * arr1
print(arr3)

print(arr3[2])
