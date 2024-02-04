# Add row
# import pandas as pd
#
# student_dict = {'Name': ['Kate', 'Harry', 'Sheila'], 'Age': [10, 11, 12], 'Marks': [85, 77, 91]}
#
# # create DataFrame from dict
# student_df = pd.DataFrame(student_dict)
# print(student_df)
# student_df.loc[len(student_df.index)] = ['Alex', 19, 93]
# print(student_df)

# df2 = {'Name': 'Tom', 'Age': 18, 'Marks': 73}
# student_df = student_df._append(df2, ignore_index = True)
# print(student_df)


import pandas as pd

student_dict_1 = {'Name': ['Kate', 'Harry', 'Sheila'],
                  'Age': [10, 14, 12],
                  'Marks': [85, 77, 91]}

# create DataFrame from dict
df1 = pd.DataFrame(student_dict_1)
print(df1)

student_dict_2 = {'Name': ['Amy', 'Maddy'],
                  'Age': [19, 12],
                  'Marks': [93, 81]
                  }
df2 = pd.DataFrame(student_dict_2)
print(df2)
df3 = pd.concat([df1, df2], ignore_index=True)

print(df3)
