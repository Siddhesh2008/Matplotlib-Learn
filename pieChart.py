import matplotlib.pyplot as plt
import numpy as np

#pie chart = circular chart divided into slices to illustrate numerical proportion

categories = ['Category A', 'Category B', 'Category C', 'Category D']
values=np.array([25, 35, 20, 20])
colors=['#ff9999','#66b3ff','#99ff99','#ffcc99']  #custom colors for each slice

plt.pie(values, labels=categories, colors=colors, autopct='%1.1f%%',
        explode=(0,0,0,0.1), shadow=True, startangle=90)
plt.title('Pie Chart Example')
plt.show()