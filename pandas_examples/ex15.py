import pandas as pd

# Sample data
data = {
    'Group': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Value': [10, 15, 20, 25, 30, 35]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate the group-wise average
grouped_data = df.groupby('Group')['Value'].mean()

# Display the result
print(grouped_data)
