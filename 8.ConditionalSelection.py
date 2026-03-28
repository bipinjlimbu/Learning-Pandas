import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)

# Single condition
print("Rows where Age is greater than 30:\n")
age_greater_than_30 = df[df['Age'] > 30]
print(age_greater_than_30)

# Multiple conditions
print("\nRows where Age is greater than 30 and City is 'Chicago':\n")
age_greater_than_30_and_chicago = df[(df['Age'] > 30) & (df['City'] == 'Chicago')]
print(age_greater_than_30_and_chicago)