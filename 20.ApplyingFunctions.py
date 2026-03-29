import pandas as pd
import numpy as np

data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
}
df = pd.DataFrame(data)

def square(x):
    return x ** 2

df['B'] = df['B'].apply(square)
print("Squared values in column B:\n")
print(df)