"""
Pivot table examples
"""


import pandas as pd


def main():
    df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                             "bar", "bar", "bar", "bar"],
                       "B": ["one", "one", "one", "two", "two",
                             "one", "one", "two", "two"],
                       "C": ["small", "large", "large", "small",
                             "small", "large", "small", "small",
                             "large"],
                       "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                       "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})
    print(df.to_string())
    print("##################")

    table = pd.pivot_table(df,
                           values='D',
                           index=['A', 'B'],
                           columns=['C'],
                           aggfunc="sum")
    print(table)
    print("##################")

    table = pd.pivot_table(df,
                           values='D',
                           index=['A', 'B'],
                           columns=['C'],
                           aggfunc="sum",
                           fill_value=0)
    print(table)
    print("##################")

    table = pd.pivot_table(df,
                           values=['D', 'E'],
                           index=['A', 'C'],
                           aggfunc={'D': "mean", 'E': "sum"})
    print(table)
    print("##################")


if __name__ == "__main__":
    main()

# EOF



