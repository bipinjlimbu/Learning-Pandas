import pandas as pd
import numpy as np

# Sample DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, np.nan, 35, 40, np.nan],
    'City': ['New York', 'Los Angeles', np.nan, 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)

# Finding missing values
print("DataFrame with missing values:\n")
print(df)

# Checking for missing values
print("\nChecking for missing values:\n")
missing_values = df.isna()
print(missing_values)

# Counting missing values in each column
print("\nCounting missing values in each column:\n")
missing_values_count = df.isna().sum()
print(missing_values_count)

# Checking if any missing values exist in the Rows of DataFrame
print("\nFinding if any missing values exist in the DataFrame:\n")
any_missing_values = df.isna().any(axis=1)
print(any_missing_values)

# Finding the total number of missing values in the DataFrame
print("\nTotal number of missing values in the DataFrame:\n")
total_missing_values = df.isna().sum().sum()
print(total_missing_values)