import matplotlib.pyplot as plt
import numpy as np
#grid()=>to add grid lines
X = np.array([1, 2, 3, 4, 5])
Y = np.array([1, 4, 9, 16, 25])

plt.plot(X, Y)
plt.grid()   #can be used with both x and y axis,linewidth, color, linestyle, alpha, which, axis
plt.show()