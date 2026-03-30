import pandas as pd
from Project3 import df

# Finding the anime with the longest duration in months

max = df['Months'] == df['Months'].max()
print("\nAnime with the longest duration in months:\n")
print(df[max])