import pandas as pd
from Project3 import df

# Finding the anime with the highest score

max = df['Score'] == df['Score'].max()
print("\nAnime with the highest score:\n")
print(df[max])