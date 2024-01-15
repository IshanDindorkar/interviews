import numpy as np


def main():
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6]])
    print("##############################")

    combined = np.concatenate((arr1, arr2), axis=0)
    print(combined)
    print("##############################")

    arr2 = arr2.reshape(2, 1)
    combined = np.concatenate((arr1, arr2), axis=1)
    print(combined)
    print("##############################")


if __name__ == "__main__":
    main()

# EOF
