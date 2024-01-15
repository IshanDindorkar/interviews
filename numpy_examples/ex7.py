import numpy as np


def main():
    arr = np.full(shape=(3, 3), fill_value=5)
    print(arr)

    arr_cp = arr.copy()
    print(arr_cp)

    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6]])

    combined = np.concatenate((arr1, arr2), axis=0)
    print(combined)


if __name__ == "__main__":
    main()

# EOF
