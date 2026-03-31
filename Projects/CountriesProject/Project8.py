import pandas as pd
from countries_csv import df

# Finding the number of countries with missing political leader information

count = df['political_leader'].isna().sum()
print(f"Number of countries with missing political leader information: {count}")