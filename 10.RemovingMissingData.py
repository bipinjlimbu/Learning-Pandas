import pandas as pd
import numpy as np

# Sample DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, np.nan, 35, 40, np.nan],
    'City': ['New York', np.nan, np.nan, 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)

# Removing rows with missing values
print("DataFrame after removing rows with missing values:\n")
df_dropped_rows = df.dropna()
print(df_dropped_rows)

# Removing columns with missing values
print("\nDataFrame after removing columns with missing values:\n")
df_dropped_columns = df.dropna(axis=1)
print(df_dropped_columns)

# Removing rows with missing values using a threshold
print("\nDataFrame after removing rows with at least 2 non-missing values:\n")
df_dropped_threshold = df.dropna(thresh=2)
print(df_dropped_threshold)