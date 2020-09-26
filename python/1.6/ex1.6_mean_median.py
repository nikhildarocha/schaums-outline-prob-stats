import numpy as np
import statistics

data = np.array([25000, 30000, 40000, 153000])
frequency = np.array([5, 7, 3,  1])



mul = data*frequency
print(mul)

total = sum(frequency)

print(total)

mean = sum(mul)/total
print(mean)

for i in range(len(frequency)-1):
    frequency[i+1] = frequency[i] + frequency[i+1]
    
print(frequency)

n = frequency[len(frequency)-1]
 
median_value = 0

if n%2 != 0:
    print("Odd number")
    median_value = (n + 1)/2
    print(median_value)
elif n%2 == 0:
    print("Even number")
    median_value = ((n/2) + (n/2)+1)/2
    print("median value is " + str(median_value))
else:
    print("The number is neither even nor odd")
    
sum_match_median = 0

for i in range(len(frequency)-1):
    sum_match_median = frequency[i]
    if sum_match_median <= median_value:
        index_of_frequency_array = list(frequency).index(sum_match_median)
        print(sum_match_median)

print(index_of_frequency_array)     
calculated_median_index = index_of_frequency_array + 1
print(calculated_median_index)
print("Index of data array " + str(data[index_of_frequency_array]))

print("Calculated median is approximately " + str(data[calculated_median_index]))
print("Median through library is " + str(statistics.median(data)))
print("Median low is " + str(statistics.median_low(data)))

    
    