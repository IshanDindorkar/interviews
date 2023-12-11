# import pandas as pd
#
# df = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [4, 5, 6],
#     'C': [7, 8, 9]
# })
#
# # Select the element in the first row and second column
# print(df.to_string())
# print(df.iloc[0, 1])


# import pandas as pd
#
# student_dict = {'Name': ['Kate', 'Harry', 'Sheila'], 'Age': [10, 14, 12], 'Marks': [85, 77, 91]}
#
# # create DataFrame from dict
# df = pd.DataFrame(student_dict)
# print(df)
# print(df.iloc[[0, 2]])



# import pandas as pd
#
# df = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [4, 5, 6],
#     'C': [7, 8, 9]
# }, index=['X', 'Y', 'Z'])
#
# # Select the element in the row with label 'X' and column with label 'B'
# print(df.to_string())
# print(df.loc['X', 'B'])
# # print(df["A"].loc[df.A == 2])


import pandas as pd

student_dict = {'Name': ['Kate', 'Harry', 'Sheila'], 'Age': [10, 14, 12], 'Marks': [85, 77, 91]}

# create DataFrame from dict
df = pd.DataFrame(student_dict)
print(df)

print(df.loc[df.Name=='Kate'])
