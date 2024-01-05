import pandas as pd

# Creating a MultiIndex from tuples
index_tuples = [('A', 1), ('A', 2), ('B', 1), ('B', 2)]
multi_index = pd.MultiIndex.from_tuples(index_tuples,
                                        names=['Letter', 'Number'])

# Creating a DataFrame with a MultiIndex
data = {'Value': [10, 20, 30, 40]}
df = pd.DataFrame(data, index=multi_index)

print("DataFrame with MultiIndex:")
print(df)

"""
Letter Number       
A      1          10
       2          20
B      1          30
       2          40
"""

# Stack: Convert the DataFrame to a long format
stacked_df = df.stack()
print("\nStacked DataFrame:")
print(stacked_df)

"""
Letter  Number       
A       1       Value    10
        2       Value    20
B       1       Value    30
        2       Value    40
"""

# Unstack: Convert the DataFrame back to the original wide format
unstacked_df = stacked_df.unstack()
print("\nUnstacked DataFrame:")
print(unstacked_df)

"""
               Value
Letter Number       
A      1          10
       2          20
B      1          30
       2          40
"""