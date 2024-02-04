"""
df2 is  a subset of df1.
get the rows of df1 which are not in df2
"""


import pandas as pd

# Creating two sample DataFrames
df1 = pd.DataFrame({'key': ['A', 'B', 'C'],
                    'value': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B'],
                    'value': [4, 5]})

print(df1.to_string())
print(df2.to_string())

# Merge df1 and df2 with indicator=True
merged_df = pd.merge(df1, df2,
                     on='key',
                     how='outer',
                     indicator=True)
print(merged_df.to_string())

# Selecting rows from df1 where '_merge' is 'left_only'
rows_not_in_df2 = (merged_df[merged_df['_merge'] == 'left_only']
                   .drop('_merge', axis=1))

print("Rows in df1 not in df2:")
print(rows_not_in_df2)

"""
Rows in df1 not in df2:
  key  value_x  value_y
2   C        3      NaN
"""
