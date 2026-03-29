import pandas as pd
import numpy as np

data1 = {
    'A':['A0', 'A1', 'A2', 'A3'],
    'B':['B0', 'B1', 'B2', 'B3'],
    'C':['C0', 'C1', 'C2', 'C3'],
    'D':['D0', 'D1', 'D2', 'D3']
}

data2 = {
    'A':['A4', 'A5', 'A6', 'A7'],
    'B':['B4', 'B5', 'B6', 'B7'],
    'C':['C4', 'C5', 'C6', 'C7'],
    'D':['D4', 'D5', 'D6', 'D7']
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Concatenating DataFrames vertically (default)
print("Concatenated DataFrame (vertical):\n")
concatenated_vertical = pd.concat([df1, df2]).reset_index(drop=True)
print(concatenated_vertical)

# Concatenating DataFrames horizontally
print("\nConcatenated DataFrame (horizontal):\n")
concatenated_horizontal = pd.concat([df1, df2], axis=1)
print(concatenated_horizontal)