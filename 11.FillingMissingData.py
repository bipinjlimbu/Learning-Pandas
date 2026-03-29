import pandas as pd
import numpy as np

# Sample DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, np.nan, 35, 40, np.nan],
    'City': ['New York', 'Los Angeles', np.nan, 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)

# Filling missing values with a specific value
print("DataFrame after filling missing values with 'Unknown':\n")
df_filled_value = df.fillna('Unknown')
print(df_filled_value)