#Table of frequency, mean, variance, standard deviation, mean, median, and quartiles, the number of drug absorption times per minute for 10 people
#139 134 159 163 138 115 106 124 124 108
import numpy as np
data = [106, 108, 115, 124, 124, 134, 138, 139, 159, 163]

# Middle
median = np.median(data)

# Average
mean = np.mean(data)

# Variance
variance = np.var(data)

# standard deviation
std_dev = np.std(data)

# The smallest and largest value
min_value = min(data)
max_value = max(data)

# First, second and third quarters
q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)  
q3 = np.percentile(data, 75)

print("Middle: ", median)
print("Average: ", mean)
print("Variance: ", variance)
print("standard deviation: ", std_dev)
print("The smallest value: ", min_value)
print("The largest value: ", max_value)
print("First quarters: ", q1)
print("second quarters (Middle): ", q2)
print("third quarters: ", q3)