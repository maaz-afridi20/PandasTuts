"""
linear Plot :
ye humein aaik line ki tarah graph dega jo b data ho us mein 

we have to use .plot() for linear graph.

"""

import matplotlib.pyplot as plt
# we can also do like this

# form matplotlib import pyplot as plt

y = [80, 48, 81, 90, 100]
x = [40,24,25,15,50]

plt.plot(x,y)
plt.show()

plt.bar(x,y,color='green')


