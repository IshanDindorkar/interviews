import numpy as np
import pandas as pd


def main():
    data = {
        "col1": ["A", "A", "B", np.nan, "D", "C"],
        "col2": [2, 1, 9, 8, 7, 4],
        "col3": [0, 1, 9, 4, 2, 3],
        "col4": ["a", "B", "c", "D", "e", "F"]
    }

    df = pd.DataFrame(data)
    print(df)

    print("###############")

    print("df.sort_values(by=['col1'], inplace=True)")
    df.sort_values(by=["col1"], inplace=True)
    print(df)

    print("###############")

    print("df.sort_values(by=['col1'], inplace=True, ascending=False)")
    df.sort_values(by=["col1"], inplace=True, ascending=False)
    print(df)


if __name__ == "__main__":
    main()

# EOF
