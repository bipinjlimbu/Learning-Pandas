import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)

# Selecting a single row
print("Selecting the row with index 2:")
row_index_2 = df.loc[2]
print(row_index_2)

# Selecting multiple rows
print("\nSelecting rows with index 1 and 3:")
rows_index_1_and_3 = df.loc[[1, 3]]
print(rows_index_1_and_3)

# Selecting rows range
print("\nSelecting rows from index 1 to 3:")
rows_index_1_to_3 = df.loc[1:3]
print(rows_index_1_to_3)