import numpy as np



data = np.array([1 ,2 ,3 ,4,5,6 ])
frequency = np.array([8,14,7,12,3,1])

mul = data*frequency
print(mul)

total = sum(frequency)

print(total)

mean = sum(mul)/total
print(mean)