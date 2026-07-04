import matplotlib.pyplot as plt
import numpy as np
X = np.array([1, 2, 3, 4, 5])
Y = np.array([1, 4, 9, 16, 25])

plt.plot(X, Y,marker='o', color='r', linestyle='--', linewidth=2, markersize=8, 
         label='Data Points',markerfacecolor='blue', markeredgecolor='black',
         markeredgewidth=1)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Customized Plot')
plt.legend()
plt.show()