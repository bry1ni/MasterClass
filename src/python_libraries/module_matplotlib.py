"""
Module: Matplotlib for Data Visualization
Course: Data Manipulation & Python Libraries
"""

import matplotlib.pyplot as plt

# Introduction to Matplotlib
# Plotting a simple line graph
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# Plotting Bar Graphs
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

plt.bar(categories, values)
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# Plotting Histograms
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

plt.hist(data, bins=4)
plt.title('Histogram')
plt.xlabel('Data')
plt.ylabel('Frequency')
plt.show()

# Customizing Plots
plt.plot(x, y, color='green', linestyle='--', marker='o')
plt.title('Customized Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

# Practical Examples
# Example 1: Plotting multiple lines in one graph
x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 4, 5, 6]

x2 = [1, 2, 3, 4, 5]
y2 = [10, 20, 25, 30, 35]

plt.plot(x1, y1, label='Line 1', color='blue')
plt.plot(x2, y2, label='Line 2', color='red')
plt.title('Multiple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()

# Example 2: Scatter plot with customized points
x = [5, 7, 8, 5, 6, 7]
y = [7, 4, 3, 8, 9, 2]
sizes = [100, 200, 300, 400, 500, 600]

plt.scatter(x, y, s=sizes, color='purple')
plt.title('Customized Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
