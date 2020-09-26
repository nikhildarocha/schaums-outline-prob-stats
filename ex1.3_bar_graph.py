from matplotlib import  pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
cities = ['Philadelphia', 'Suburbs', 'PA', 'NJ', 'Elsewhere']
students = [225, 100, 60, 75, 40]
fig, ax = plt.subplots(figsize =(10, 7)) 
ax.bar(cities,students)
plt.show()