import pandas as pd
import numpy as np

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
print("DataFrame from a dictionary:\n")
df_from_dict = pd.DataFrame(data)
print(df_from_dict)

# Creating a DataFrame from a list of dictionaries
data_list = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'},
    {'Name': 'David', 'Age': 40, 'City': 'Houston'},
    {'Name': 'Eve', 'Age': 45, 'City': 'Phoenix'}
]
print("\nDataFrame from a list of dictionaries:\n")
df_from_list = pd.DataFrame(data_list)
print(df_from_list)

columns = ['Name', 'Age', 'City']
# Creating a DataFrame from a NumPy array
data_array = np.array([
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago'],
    ['David', 40, 'Houston'],
    ['Eve', 45, 'Phoenix']
])
print("\nDataFrame from a NumPy array:\n")
df_from_array = pd.DataFrame(data_array, columns=columns)
print(df_from_array)

# Creating a DataFrame from a list of lists
data_list_of_lists = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago'],
    ['David', 40, 'Houston'],
    ['Eve', 45, 'Phoenix']
]
print("\nDataFrame from a list of lists:\n")
df_from_list_of_lists = pd.DataFrame(data_list_of_lists, columns=columns)
print(df_from_list_of_lists)