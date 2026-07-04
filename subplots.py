import matplotlib.pyplot as plt
import numpy as np

#Figure=The entire Canvas
#Subplots=Multiple plots in a single canvas
#Ax=A single plot in a canvas

x=np.array([0,1,1,2,3,4,5,6,7,7,8])

figure,axes=plt.subplots(2,2)  #2 rows and 2 columns
axes[0,0].plot(x,x**2,color='red',marker='o',linestyle='dashed',linewidth=2,markersize=5,label='x^2')
axes[0,0].set_title('x^2')
axes[0,1].plot(x,x**3,color='green',marker='o',linestyle='dashed',linewidth=2,markersize=5,label='x^3')
axes[0,1].set_title('x^3')
axes[1,0].plot(x,x**4,color='blue',marker='o',linestyle='dashed',linewidth=2,markersize=5,label='x^4')
axes[1,0].set_title('x^4')
axes[1,1].plot(x,x**5,color='yellow',marker='o',linestyle='dashed',linewidth=2,markersize=5,label='x^5')
axes[1,1].set_title('x^5')
plt.tight_layout()  #to avoid overlapping of subplots
plt.show()