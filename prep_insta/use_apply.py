import pandas as pd


def main():
    data = {
        "A": [1, 2, 3],
        "B": [4, 5, 6],
        "C": [7, 8, 9]
    }

    df = pd.DataFrame(data=data, index=["X", "Y", "Z"])
    print(df.to_string())

    print("################")
    new_df = df.apply(lambda x: x ** 2,
                      axis="columns")
    print(new_df.to_string())

    print("################")
    new_df = df[["C"]].apply(lambda x: x ** 2,
                             axis="columns")
    print(new_df.to_string())


if __name__ == "__main__":
    main()

# EOF
