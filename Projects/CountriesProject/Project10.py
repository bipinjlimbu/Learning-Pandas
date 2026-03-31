import pandas as pd
from countries_csv import df

# Finding the top 5 African countries with the highest population

check = df['region'].str.contains('Africa')
df_africa = df[check]
sorted_df = df_africa.sort_values(by='population', ascending=False)

print("\nTop 5 African Countries with the highest population:\n")
print(sorted_df[['country', 'population']].head(5))