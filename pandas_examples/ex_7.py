import pandas as pd


def main():
    data = {
        "colX": ["class 1", "class 2", "class 3", "class 2"],
        "colY": ["cat 1", "cat 1", "cat 2", "cat 3"]
    }
    df = pd.DataFrame(data)

    print(pd.pivot_table(df, index=["colX"],
                         columns=["colY"],
                         aggfunc=len,
                         fill_value=0))


if __name__ == "__main__":
    main()

# EOF
