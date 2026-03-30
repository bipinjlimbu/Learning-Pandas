import pandas as pd
from Project1 import df

# Feature Extraction: Extracting the timestamp from the 'Title' column

def extract_timestamp(txt):
    data = ''
    for i in range(len(txt)):
        if txt[i] == ')':
            for j in range(i+1, i+20):
                data += txt[j]
                
    return data

df['Timestamp'] = df['Title'].apply(lambda x: extract_timestamp(x))

if __name__ == "__main__":
    print("\nFirst 5 rows of the DataFrame with Timestamp:\n")
    print(df.head())