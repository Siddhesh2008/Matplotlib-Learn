import matplotlib.pyplot as plt
import numpy as np

#histogram=A visual representation of the distribution of data 
#they group values into bins (intervals) and count how many values fall into each bin

scores=np.random.normal(loc=80, scale=10, size=100)  #normal distribution
scores=np.clip(scores,0,100)  #clip values to be between 0 and 100
plt.hist(scores,bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.title('Histogram Example')
plt.xlabel('Scores')
plt.ylabel('Frequency')
plt.show()