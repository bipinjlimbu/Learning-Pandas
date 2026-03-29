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