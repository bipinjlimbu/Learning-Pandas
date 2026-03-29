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

pivot_table = pd.pivot_table(df, values=['Sales', 'Quantity'], index=['Category'], columns=['Store'], aggfunc='sum')
print("Pivot Table:\n")
print(pivot_table)