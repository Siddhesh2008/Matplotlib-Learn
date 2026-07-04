import matplotlib.pyplot as plt
import numpy as np
X = np.array([1, 2, 3, 4, 5])
Y = np.array([1, 4, 9, 16, 25])

plt.bar(X, Y, color='blue', edgecolor='black', width=0.5, alpha=0.7)
plt.title('Bar Chart Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()        #barh can be used for horizontal chart