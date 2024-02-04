# # Slicing a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get elements from index 2 to 5 (exclusive)
sliced_numbers = numbers[2:5]

print("Sliced Numbers:", sliced_numbers)
#

# Dicing a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get every second element starting from index 1
diced_numbers = numbers[1::2]

print("Diced Numbers:", diced_numbers)

# Dicing a tuple
colors = ('red', 'green', 'blue', 'yellow', 'orange')

# Get every second element starting from index 0
diced_colors = colors[::2]

print("Diced Colors:", diced_colors)
