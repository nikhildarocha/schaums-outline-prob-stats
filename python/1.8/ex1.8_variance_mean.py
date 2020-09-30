import numpy as np
import statistics


list_A = np.array([3, 5, 8, 9, 10, 12, 13, 15, 20])

product_one = 0

for i in list_A:
    product_one= i*i  + product_one

print("product one")
print(product_one)

print("sum the whole squared divided by n")

sum_two = 0

for i in list_A:
    sum_two += i

print(sum_two)
print(sum(list_A))

sum_two_squared = sum_two*sum_two

print(sum_two_squared)

sum_two_squared_by_n = sum_two_squared/len(list_A)

print(sum_two_squared_by_n)

print("variance through simplified formula is ")

variance_simplified = (product_one - sum_two_squared_by_n)/(len(list_A) -1)

print(int(variance_simplified))

