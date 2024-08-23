"""
Module: Numpy for Numerical Data
Course: Data Manipulation & Python Libraries
"""

# Introduction to Numpy
import numpy as np

# Creating Numpy Arrays
array_1d = np.array([1, 2, 3, 4, 5, 6])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# print("1D Array:", array_1d)
# print("2D Array:\n", array_2d)

# # Basic Operations on Numpy Arrays
# array_sum = array_1d + 10
# array_product = array_2d * 2

# print("Array Sum:", array_sum)
# print("Array Product:\n", array_product)

# Reshaping and Slicing Numpy Arrays
#reshaped_array = array_3d.reshape(3, 2)
# sliced_array = array_1d[1:4]
# slice_2d = array_3d[2, 1:]
# print(slice_2d)

# print("Reshaped Array:\n", reshaped_array)
# print("Sliced Array:", sliced_array)

# Statistical Operations
# mean_value = np.mean(array_1d)
# max_value = np.max(array_2d)
# min_value = np.min(array_2d)

# print("Mean Value:", mean_value)
# print("Max Value in 2D Array:", max_value)
# print("Min Value in 2D Array:", min_value)

# Practical Examples
# Example 1: Summing elements across rows in a 2D array
# row_sums = np.sum(array_2d, axis=1)
# print("Row Sums:", row_sums)

# Example 2: Creating a matrix of zeros and ones
zeros_matrix = np.zeros((3, 3))
ones_matrix = np.ones((3, 3))

print("Zeros Matrix:\n", zeros_matrix)
print("Ones Matrix:\n", ones_matrix)
