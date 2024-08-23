"""
Module: Pandas for Data Manipulation
Course: Data Manipulation & Python Libraries
"""

import pandas as pd
import numpy as np

# Introduction to Pandas Series and DataFrames
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [24, 27, 22, 32, 29],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

<<<<<<< Updated upstream
df.to_csv('output.csv', index=False)

# Importing and Exporting Data
# Importing from a CSV file
#df_imported = pd.read_csv('example.csv')

# # Exporting to an Excel file
# df.to_excel('output.xlsx', index=False)
=======
# Exporting to an Excel file
df.to_csv('example.csv', index=False)

# Importing and Exporting Data
# Importing from a CSV file
df_imported = pd.read_csv('example.csv')
print("Imported DataFrame:\n", df_imported)
>>>>>>> Stashed changes

# # Basic Data Operations
# # Sorting data by age
# df_sorted = df.sort_values(by='Age')
# print("Sorted DataFrame:\n", df_sorted)

# # Filtering data for people older than 25
# df_filtered = df[df['Age'] > 25]
# print("Filtered DataFrame:\n", df_filtered)

# # Grouping data by city
# df_grouped = df.groupby('City').mean()
# print("Grouped DataFrame:\n", df_grouped)

# # Handling Missing Data
# df_missing = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6]})
# print("DataFrame with Missing Values:\n", df_missing)

# # Filling missing values
# df_filled = df_missing.fillna(0)
# print("Filled Missing Values:\n", df_filled)

# # Dropping missing values
# df_dropped = df_missing.dropna()
# print("Dropped Missing Values:\n", df_dropped)

# # Practical Examples
# # Example 1: Concatenating DataFrames
# df2 = pd.DataFrame({'Name': ['Frank', 'Grace'], 'Age': [28, 33], 'City': ['Seattle', 'Miami']})
# df_combined = pd.concat([df, df2])
# print("Concatenated DataFrame:\n", df_combined)

# # Example 2: Merging DataFrames on a common column
# df_scores = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#                           'Score': [85, 78, 92, 88, 95]})
# df_merged = pd.merge(df, df_scores, on='Name')
# print("Merged DataFrame:\n", df_merged)
