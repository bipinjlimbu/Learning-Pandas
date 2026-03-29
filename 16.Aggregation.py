import pandas as pd
import numpy as np

data = {
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Store': ['X', 'Y', 'X', 'Y', 'X'],
    'Sales': [100, 200, 150, 250, 120],
    'Quantity': [10, 20, 15, 25, 12],
    'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'])
}
df = pd.DataFrame(data)

aggregated_df = df['Sales'].agg(['sum', 'mean', 'min', 'max', 'count', 'std', 'median', 'var'])
print("Aggregated DataFrame for df:\n")
print(aggregated_df)