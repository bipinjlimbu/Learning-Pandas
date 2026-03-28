import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [50000, 60000, 70000, 80000, 90000],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales']
}
df = pd.DataFrame(data)

# Removing a column
print("DataFrame after removing the 'Department' column:")
df_dropped_column = df.drop('Department', axis=1)   
print(df_dropped_column)

#Permanently removing a column
print("\nDataFrame after permanently removing the 'Department' column:")
df.drop(['Salary','Department'], axis=1, inplace=True)
print(df)

# Removing a row
print("\nDataFrame after removing the row with index 2:")
df_dropped_row = df.drop(2, axis=0)
print(df_dropped_row)

# Permanently removing a row
print("\nDataFrame after permanently removing the row with index 2:")
df.drop([2,4], axis=0, inplace=True)
print(df)