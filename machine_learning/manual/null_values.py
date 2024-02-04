import pandas as pd

# Sample DataFrame with null values
data = {'A': [1, 2, None, 4, 5],
        'B': [None, 7, 8, 9, 10]}
df = pd.DataFrame(data)

# Check for null values
print("Null Values in DataFrame:")
print(df.isnull())

# EOF
