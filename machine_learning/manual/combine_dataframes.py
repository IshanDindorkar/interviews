# # Merge dataframes
#
# import pandas as pd
#
# df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
# df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value': [4, 5, 6]})
#
# print(df1.to_string())
# print(df2.to_string())
#
# merged_df = pd.merge(df1, df2, on='key', how='outer')
# # merged_df = pd.merge(df1, df2, on='key', how='inner')
# print(merged_df.to_string())
#

import pandas as pd

df1 = pd.DataFrame({'value': [1, 2, 3]}, index=['A', 'B', 'C'])
df2 = pd.DataFrame({'value': [4, 5, 6]}, index=['A', 'B', 'D'])

print(df1.to_string())
print(df2.to_string())

joined_df = df1.join(df2, how='outer', lsuffix='_left', rsuffix='_right')
print(joined_df.to_string())