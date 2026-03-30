import pandas as pd
from countries_csv import df

# Finding the country with the highest population

max = df['population'] == df['population'].max()
print("\nCountry with the highest population:\n")
print(df['country'][max])