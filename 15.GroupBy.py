import pandas as pd
import numpy as np

data1 = {
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Store': ['X', 'Y', 'X', 'Y', 'X'],
    'Sales': [100, 200, 150, 250, 120],
    'Quantity': [10, 20, 15, 25, 12],
    'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'])
}

data2 = {
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Store': ['X', 'Y', 'X', 'Y', 'X'],
    'Sales': [110, 210, 160, 260, 130],
    'Quantity': [11, 21, 16, 26, 13],
    'Date': pd.to_datetime(['2023-01-06', '2023-01-07', '2023-01-08', '2023-01-09', '2023-01-10'])
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Grouping by 'Category' and calculating the sum of 'Sales'
grouped_category = df1.groupby('Category')['Sales'].sum()
print("Total Sales by Category:\n")
print(grouped_category)

# Grouping by 'Store' and calculating the sum of 'Sales'
grouped_store = df1.groupby('Store')['Sales'].sum()
print("\nTotal Sales by Store:\n")
print(grouped_store)

# Grouping by 'Category' and 'Store' and calculating the sum of 'Sales'
grouped_category_store = df1.groupby(['Category', 'Store'])['Sales'].sum()
print("\nTotal Sales by Category and Store:\n")
print(grouped_category_store)