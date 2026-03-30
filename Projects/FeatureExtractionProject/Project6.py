import pandas as pd
from Project3 import df

# Finding the anime with the highest number of episodes

max = df['Episodes'] == df['Episodes'].max()
print("\nAnime with the highest number of episodes:\n")
print(df[max])