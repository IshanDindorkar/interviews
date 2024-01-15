"""
Create different distributions using Numpy
and create Panda dataframes
"""


import numpy as np
import pandas as pd


def main():
    arr1 = np.arange(12).reshape(3, 4)
    df = pd.DataFrame(arr1)
    print(df.to_string())

    arr2 = np.random.rand(100, 100)
    df = pd.DataFrame(arr2)
    print(df.shape)
    print(df.head())

    arr3 = np.random.randint(1, 100, 25)
    arr3 = arr3.reshape((5, 5))
    df = pd.DataFrame(arr3)
    print(df.head())


if __name__ == "__main__":
    main()

# EOF
