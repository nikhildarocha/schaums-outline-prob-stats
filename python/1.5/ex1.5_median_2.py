import numpy as np
import statistics

data = np.array([ 72.5, 77.5, 82.5, 87.5, 92.5, 97.5, 102.5, 107.5])

frequency = np.array([3, 6, 8, 5, 7, 3, 0, 3])

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
print("Median through library  is " + str(statistics.median(data)))

    
    