import pandas as pd
from countries_csv import df

# Finding the number of countries with 'Republic' in their name

count = df['country'].str.contains('Republic').sum()
print(f"Number of countries with 'Republic' in their name: {count}")