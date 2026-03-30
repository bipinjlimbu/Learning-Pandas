import pandas as pd
from Project3 import df

# Finding Top 5 anime with the highest number of episodes

episode_sort = df.sort_values(by='Episodes', ascending=False).reset_index(drop=True)
print("Top 5 Animes with the highest number of episodes:\n")
print(episode_sort.head())