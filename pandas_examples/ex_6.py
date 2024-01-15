import pandas as pd


def main():
    df = pd.DataFrame({
        "a": ["A", "A", "B", "B", "B", "C"],
        "b": [1, 2, 5, 5, 4, 6]
    })
    print(df.to_string())
    print("##################")

    df_grouped = (df.groupby("a")["b"]
                  .apply(list)
                  .reset_index(name="new"))
    print(df_grouped)


"""
   a  b
0  A  1
1  A  2
2  B  5
3  B  5
4  B  4
5  C  6
##################
   a        new
0  A     [1, 2]
1  B  [5, 5, 4]
2  C        [6]
"""

if __name__ == "__main__":
    main()

# EOF
