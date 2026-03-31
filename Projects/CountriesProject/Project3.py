import pandas as pd
from countries_csv import df

# Finding the capital city of the country with the lowest population

min = df['population'] == df['population'].min()
print("\nCapital City of the Country with the lowest population:\n")
print(df['capital_city'][min])