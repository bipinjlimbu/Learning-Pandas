import pandas as pd
from CSV import df

# Feature Extraction: Extracting the number of episodes from the 'Title' column

def extract_episode(txt):
    check = False
    data = ''
    for i in txt:
        if i == ')':
            break
        
        if i == '(':
            check = True
            continue
            
        if check:
            data += i
              
    return data

df['Episodes'] = df['Title'].apply(lambda x: extract_episode(x))
df['Episodes'] = df['Episodes'].str.replace(' eps', '').astype(int)

if __name__ == "__main__":
    print("\nFirst 5 rows of the DataFrame with Episodes:\n")
    print(df.head())