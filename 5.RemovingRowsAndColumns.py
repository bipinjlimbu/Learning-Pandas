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
df.drop('Department', axis=1, inplace=True)
print(df)