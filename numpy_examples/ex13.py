import numpy as np
import pandas as pd


def main():
    seq_arr = np.arange(12).reshape(3, 4)
    print(seq_arr)

    # Converting array to dataframe
    df = pd.DataFrame(seq_arr, columns=["col1", "col2", "col3", "col4"])
    print(df.to_string())

    print("########################################")

    rand_arr = np.random.rand(3, 3)
    print(rand_arr)

    print("########################################")

    rand_arr = np.random.randint(1, 100, 25).reshape(5, 5)
    print(rand_arr)


if __name__ == "__main__":
    main()

# EOF
