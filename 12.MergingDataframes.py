import pandas as pd
import numpy as np

employees = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR']
}
salaries = {
    'ID': [1, 2, 3, 6, 7],
    'Salary': [50000, 60000, 55000, 70000, 65000]
}

df_employees = pd.DataFrame(employees)
df_salaries = pd.DataFrame(salaries)

# Merging DataFrames on the 'ID' column
print("Merged DataFrame using inner join:\n")
merged_inner = pd.merge(df_employees, df_salaries, on='ID', how='inner')
print(merged_inner)

# Merging DataFrames using outer join
print("\nMerged DataFrame using outer join:\n")
merged_outer = pd.merge(df_employees, df_salaries, on='ID', how='outer')
print(merged_outer)

# Merging DataFrames using left join
print("\nMerged DataFrame using left join:\n")
merged_left = pd.merge(df_employees, df_salaries, on='ID', how='left')
print(merged_left)