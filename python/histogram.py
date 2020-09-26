from matplotlib import  pyplot as plt
import numpy as np

a = np.array([225, 100, 60, 75, 40])
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize =(10, 7)) 
ax.hist(a, bins =10) 
  
# Show plot 
plt.show() 