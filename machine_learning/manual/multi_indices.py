import pandas as pd

student_dict = {'Name': ['Kate', 'Harry', 'Sheila'], 'Age': [10, 11, 12], 'Marks': [85, 77, 91]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict)
print(student_df)

# set index using column
student_df = student_df.set_index(['Name', 'Marks'])
print(student_df)

student_df = student_df.reset_index()
print(student_df)