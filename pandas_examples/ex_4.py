import pandas as pd


def main():
    data = {
        "row": ["00000 UNITED STATES",
                "01000 ALABAMA",
                "01001 Autauga County, AL",
                "01003 Baldwin County, AL"]
    }

    df = pd.DataFrame(data)
    print(df)

    df[["code", "location"]] = (df["row"]
                                .str
                                .split(n=1, expand=True))
    print(df[["code", "location"]])


if __name__ == "__main__":
    main()

# EOF
