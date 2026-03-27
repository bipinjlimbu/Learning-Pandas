import numpy as np
import pandas as pd

labels = ['a', 'b', 'c', 'd', 'e']
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
my_dict = {'1': 10, '2': 20, '3': 30, '4': 40, '5': 50}

# Creating a Series from a list
print("Series from a list:")
series_from_list = pd.Series(my_list)
print(series_from_list)

# Creating a Series from a NumPy array
print("\nSeries from a NumPy array:")
series_from_array = pd.Series(my_array, index=labels)
print(series_from_array)

# Creating a Series from a dictionary
print("\nSeries from a dictionary:")
series_from_dict = pd.Series(my_dict)
print(series_from_dict)

# Creating a Series from a scalar value
print("\nSeries from a scalar value:")
series_from_scalar = pd.Series(10, index=labels)
print(series_from_scalar)