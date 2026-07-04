import matplotlib.pyplot as plt
import numpy as np
#Scatter graph is used to plot the data points on the graph
x=np.array([0,1,1,2,3,4,5,6,7,7,8])
y=np.array([55,60,65,62,68,70,75,80,85,90,95])
y2=np.array([50,55,60,65,70,75,80,85,90,95,100])
plt.scatter(x,y,color='red',marker='o',s=50,linewidth=2,edgecolor='black',alpha=0.7,label='Class A')
plt.scatter(x,y2,color='green',marker='^',s=50,linewidth=2,edgecolor='black',alpha=0.7,label='Class B')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Scatter Plot')
plt.legend()
plt.show()