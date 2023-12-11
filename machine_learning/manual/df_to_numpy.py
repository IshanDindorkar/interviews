import numpy as np
import pandas as pd

# Create a DataFrame
data = {'A': [1, 4, 7], 'B': [2, 5, 8], 'C': [3, 6, 9]}
df = pd.DataFrame(data)

# Convert DataFrame to NumPy array
numpy_array_from_df = df.to_numpy()

print("NumPy Array from DataFrame:")
print(numpy_array_from_df)
