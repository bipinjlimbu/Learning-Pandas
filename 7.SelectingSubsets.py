import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)
print("Original DataFrame:\n")
print(df)

# Subset
print("\nSubset of the DataFrame (rows with index 2 and 3, columns 'Name' and 'City'):\n")
subset = df.loc[[2, 3], ['Name', 'City']]
print(subset)