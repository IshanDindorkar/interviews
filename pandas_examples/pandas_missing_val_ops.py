import pandas as pd
import numpy as np

# Create a sample DataFrame with missing data
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, np.nan],
    'C': [1, 2, 3, 4, 5]
}

df = pd.DataFrame(data, index=["V", "W", "X", "Y", "Z"])
df_modified = df.drop(axis="columns", columns=["C"])
print("Dataframe with C column dropped")
print(df_modified.to_string())

df_modified = df.drop(axis="index", index=["Y"])
print("Dataframe with Y index dropped")
print(df_modified.to_string())

# Check for missing values using isnull and notnull
print("DataFrame with missing values:")
print(df)
print("\nChecking for missing values:")
print(df.isnull())
print("\nChecking for non-missing values:")
print(df.notnull())

# Drop rows or columns with missing values using dropna
df_dropna_rows = df.dropna()  # Drop rows with any missing values
df_dropna_cols = df.dropna(axis="columns")  # Drop columns with any missing values

print("\nDataFrame after dropping rows with missing values:")
print(df_dropna_rows)

print("\nDataFrame after dropping columns with missing values:")
print(df_dropna_cols)

# Fill missing values using fillna
df_fillna = df.fillna(value=0)  # Fill missing values with 0

print("\nDataFrame after filling missing values with 0:")
print(df_fillna)
