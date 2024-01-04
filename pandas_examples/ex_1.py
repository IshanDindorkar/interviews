"""
Example to print out column names of dataframe
"""


import pandas as pd


def main():
    data = {
        "A": [1, 2, 3, 4, 5],
        "B": [1, 2, 3, 4, 5]
    }

    df = pd.DataFrame(data)
    print(df)

    print(f"Columns in dataframe: {df.columns.values}")


if __name__ == "__main__":
    main()

# EOF
