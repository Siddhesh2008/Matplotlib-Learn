import matplotlib.pyplot as plt
import numpy as np
X = np.array([1, 2, 3, 4, 5])
Y1 = np.array([1, 4, 9, 16, 25])
Y2 = np.array([1, 2, 3, 4, 5])
Y3 = np.array([5, 4, 3, 2, 1])

plt.title('Multiple Lines Plot',fontsize=14, fontweight='bold',family="Arial")
plt.xlabel('X-axis', fontsize=12, fontweight='bold',family="Arial")
plt.ylabel('Y-axis', fontsize=12, fontweight='bold',family="Arial")
plt.tick_params(axis='both', color='black')
plt.plot(X,Y1)
plt.plot(X,Y2)
plt.plot(X,Y3)
plt.xticks(X)
plt.show()