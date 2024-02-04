import pandas as pd

# Creating two sample DataFrames
df1 = pd.DataFrame({'A': ['A0', 'A1'], 'B': ['B0', 'B1']})
df2 = pd.DataFrame({'A': ['A2', 'A3'], 'B': ['B2', 'B3']})
print(df1.to_string())
print(df2.to_string())

# Using concat to concatenate DataFrames along rows (axis=0)
concatenated_df_rows = pd.concat([df1, df2],
                                 ignore_index=True)

# Using concat to concatenate DataFrames along columns (axis=1)
concatenated_df_columns = pd.concat([df1, df2],
                                    axis=1)

print("Concatenated DataFrame along rows:")
print(concatenated_df_rows)

print("\nConcatenated DataFrame along columns:")
print(concatenated_df_columns)
