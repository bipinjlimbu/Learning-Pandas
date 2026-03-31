import pandas as pd
from countries_csv import df

min = df['population'] == df['population'].min()
print("\nCountry with the lowest population:\n")
print(df['country'][min])