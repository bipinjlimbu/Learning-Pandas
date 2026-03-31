import pandas as pd
from countries_csv import df

# Finding the political leader of the country with the second highest population

check = df['population'] == df['population'].nlargest(2).iloc[1]
print("\nPolitical Leader of the Country with the second highest population:\n")
print(df['political_leader'][check])