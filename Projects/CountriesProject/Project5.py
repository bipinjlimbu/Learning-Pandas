import pandas as pd
from countries_csv import df

# Finding the total number of regions in the dataset

region_counts = df['region'].unique().size
print("\nTotal Regions in the dataset:\n")
print(region_counts)