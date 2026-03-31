import pandas as pd
from countries_csv import df

# Finding the top 5 countries with the highest democracy score

sorted_df = df.sort_values(by='democracy_score', ascending=False)
print("\nTop 5 Countries with the highest democracy score:\n")
print(sorted_df[['country', 'democracy_score']].head(5))