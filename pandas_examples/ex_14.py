import pandas as pd

# Creating a DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data,
                  index=['row1', 'row2', 'row3'])
print(df.to_string())
print("###############")

# Accessing a specific element using labels
value = df.at['row2', 'A']
print(value)

# Accessing a specific element using integer indices
value = df.iat[1, 0]
print(value)
