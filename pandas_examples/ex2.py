import pandas as pd


def main():
    data = {
        "A": [1, 2, 3],
        "B": [4, 5, 6],
        "C": [7, 8, 9],
    }

    df = pd.DataFrame(data)
    print(df)

    print("################")

    print("df.iloc[0]")
    print(df.iloc[0])

    print("################")

    print("df.iloc[:2, :2]")
    print(df.iloc[:2, :2])

    print("################")

    print("df.iloc[-2:]")
    print(df.iloc[-2:])

    print("################")

    print("df.iloc[-2:, 1]")
    print(df.iloc[-2:, 1])


if __name__ == "__main__":
    main()

# EOF
