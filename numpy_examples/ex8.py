"""
Swapping columns
https://www.geeksforgeeks.org/how-to-swap-columns-of-a-given-numpy-array/?ref=lbp
"""


# importing Module
import numpy as np

# creating array with shape(4,3)
my_array = np.arange(12).reshape(4, 3)
print("Original array:")
print(my_array)

# swapping the column with index of
# original array
my_array[:, [2, 0]] = my_array[:, [0, 2]]
print("After swapping arrays the last column and first column:")
print(my_array)

# EOF
