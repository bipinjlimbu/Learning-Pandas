import pandas as pd
from countries_csv import df

# Finding the capital city of the country with the highest population

max = df['population'] == df['population'].max()
print("\nCapital City of the Country with the highest population:\n")
print(df['capital_city'][max])