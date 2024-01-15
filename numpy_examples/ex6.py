"""
Finding max and min values from array
"""


import numpy as np


def main():
    arr = np.arange(0, 1000)
    max_val = arr.max()
    max_val_idx = arr.argmax()
    print(f"{max_val_idx}: {max_val}")

    # Similar functions for finding minimum value


if __name__ == "__main__":
    main()

# EOF
