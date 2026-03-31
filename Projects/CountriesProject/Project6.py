import pandas as pd
from countries_csv import df

# Finding the number of countries in the Eastern Europe region

filter = df['region'] == 'Eastern Europe'
print("\nNumber of Countries in the Eastern Europe region:\n")
print(df['country'][filter].size)