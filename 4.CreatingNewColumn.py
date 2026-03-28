import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)

# Creating a new column as a Salary
print("Creating a new column 'Salary':")
df['Salary'] = [50000, 60000, 70000, 80000, 90000]
print(df)