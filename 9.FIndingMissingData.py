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