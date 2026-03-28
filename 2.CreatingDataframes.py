import pandas as pd
import numpy as np

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
print("DataFrame from a dictionary:\n")
df_from_dict = pd.DataFrame(data)
print(df_from_dict)