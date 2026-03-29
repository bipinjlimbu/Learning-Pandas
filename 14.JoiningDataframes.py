import numpy as np
import pandas as pd

# Sample DataFrames to join
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
}, index=[0, 1, 2, 3])

df2 = pd.DataFrame({
    'Age': [25, 30, 35, 40]
}, index=[2, 3, 4, 5])

#Inner Joining DataFrames
joined_df = df1.join(df2, how='inner')
print("Joined DataFrame using inner join:\n")
print(joined_df)

#Outer Joining DataFrames
joined_df_outer = df1.join(df2, how='outer')
print("\nJoined DataFrame using outer join:\n")
print(joined_df_outer)

#Left Joining DataFrames
joined_df_left = df1.join(df2, how='left')
print("\nJoined DataFrame using left join:\n")
print(joined_df_left)

#Right Joining DataFrames
joined_df_right = df1.join(df2, how='right')
print("\nJoined DataFrame using right join:\n")
print(joined_df_right)