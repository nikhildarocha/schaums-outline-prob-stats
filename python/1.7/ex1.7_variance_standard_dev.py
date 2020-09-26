import numpy as np
import statistics
import math

list_A = np.array([12, 10, 9, 9, 10])
list_B = np.array([5, 10, 16, 15, 4])

mean_A = np.mean(list_A)
mean_B = np.mean(list_B)

x1 = 12 - mean_A
x2 = 10 - mean_A
x3 = 9 - mean_A
x4 = 9 - mean_A
x5 = 10 - mean_A

xx1 = x1**2
xx2 = x2**2
xx3 = x3**2
xx4 = x4**2
xx5 = x5**2

var_AA = (xx1+xx2+xx3+xx4+xx5)/4
print(var_AA)
sd_AA = math.sqrt(var_AA)

print(sd_AA)

var_A = np.var(list_A)
print("variance of A " +str(var_A))

std_A = np.std(list_A,ddof=1)
print("standard deviation of A " +str(std_A))


var_B = np.var(list_B)
print("variance of B " + str(var_B))

std_B = np.std(list_B, ddof=1)
print("standard deviation of B " +str(std_B))