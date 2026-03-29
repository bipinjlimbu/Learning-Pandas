import pandas as pd
import numpy as np

data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
}
df = pd.DataFrame(data)

# Shape
print("Shape of the DataFrame:\n")
print(df.shape)

# Columns
print("\nColumns in the DataFrame:\n")
print(df.columns)

# Info
print("\nInformation about the DataFrame:\n")
print(df.info())

# Describe
print("\nStatistical summary of the DataFrame:\n")
print(df.describe())

# Broadcasting
print("\nAdding 10 to each element in the DataFrame:\n")
broadcasted_df = df + 10
print(broadcasted_df)