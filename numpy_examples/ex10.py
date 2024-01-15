import numpy as np


def main():
    arr1 = np.random.rand(3, 3)
    arr2 = np.random.rand(3, 3)

    arr3 = arr1 + arr2
    print(arr3)

    arr4 = arr1 - arr2
    print(arr4)


if __name__ == "__main__":
    main()

# EOF
