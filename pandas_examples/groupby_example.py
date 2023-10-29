import pandas as pd

# Create a sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'C', 'C'],
    'Value': [10, 15, 20, 25, 30, 5, 12]
}

df = pd.DataFrame(data)

# Group the data by the 'Category' column
grouped = df.groupby('Category')

# Calculate the sum for each group
sum_result = grouped['Value'].sum()

# Calculate the mean for each group
mean_result = grouped['Value'].mean()

# Calculate the count for each group
count_result = grouped['Value'].count()

# Display the results
print("Original DataFrame:")
print(df)

print("\nGrouped by 'Category' and summed:")
print(sum_result)

print("\nGrouped by 'Category' and averaged:")
print(mean_result)

print("\nGrouped by 'Category' and counted:")
print(count_result)
