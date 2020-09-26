import numpy as np


data = np.array([ 72.5, 77.5, 82.5, 87.5, 92.5, 97.5, 102.5, 107.5])

frequency = np.array([3, 6, 8, 5, 7, 3, 0, 3])

mul = data*frequency

print(mul)

total = sum(frequency)

mean = sum(mul)/total

print(mean)