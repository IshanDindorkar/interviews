import pandas as pd

# Sample data
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'C', 'C'],
    'Value': [10, 15, 20, 25, 30, 12, 18]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by 'Category' and calculate the sum of 'Value'
grouped_df = (df.groupby('Category')['Value'].sum()
              .reset_index())

# Sort the DataFrame by the sum of values in descending order
sorted_df = grouped_df.sort_values(by='Value',
                                   ascending=False)
#
# Display the result
print("Original DataFrame:")
print(df)
print("\nGrouped and Summed DataFrame:")
print(grouped_df)
print("\nSorted DataFrame:")
print(sorted_df)
