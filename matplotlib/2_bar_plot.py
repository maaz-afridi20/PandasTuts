"""
Bar Plot :

we can show bar plot using plt.bar(xAxisData,yAxisData)

some more parameters.

plt.xlabel=("anyName")  that will be written on side of plot
plt.ylabel=("anyName")  that will be written below of plot
plt.title=("anyname")   will be title of plot.
"""

import matplotlib.pyplot as plt

y = [80, 48, 81, 90, 100]
x = ["part1", 'part2', 'part3','part4','part5']


plt.xlabel("x label")
plt.ylabel("y label")
plt.title("Title..")
plt.bar(x, y)
