import pandas as pd

# Creating two sample DataFrames with the same index
df1 = pd.DataFrame({'value': [1, 2, 3]}, index=['A', 'B', 'C'])
df2 = pd.DataFrame({'value': [4, 5, 6]}, index=['A', 'B', 'D'])

# Using join to combine DataFrames based on their indices
joined_df = df1.join(df2, lsuffix='_df1', rsuffix='_df2', how='inner')

print("Joined DataFrame:")
print(joined_df)
