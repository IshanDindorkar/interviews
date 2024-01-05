import pandas as pd


def main():
    df1 = pd.DataFrame({
        "a": ["foo", "bar"],
        "b": [1, 2]
    })
    df2 = pd.DataFrame({
        "a": ["foo", "baz"],
        "b": [3, 4]
    })

    print(df1)
    print("##################")

    print(df2)
    print("##################")

    df3 = df1.merge(df2, how="inner", on="a")
    print(df3)
    print("##################")

    df4 = df1.merge(df2, how="left", on="a")
    print(df4)
    print("##################")

    df5 = df1.merge(df2, how="right", on="a")
    print(df5)
    print("##################")


if __name__ == "__main__":
    main()

# EOF
