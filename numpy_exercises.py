from statistics import mean, stdev
import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?

a[a < 0]
print(a[a < 0])

# 2. How many positive numbers are there?

a[a > 0]
print(a[a > 0])
#print(f'a array positive numbers == {a >= 0}')

# 3. How many even positive numbers are there?

a[(a > 0) & (a % 2 ==0)]
print(a[(a > 0) & (a % 2 ==0)])
#print(f'a array even positive numbers == {a >= 0 & a % 2 == 0}')

# 4. If you were to add 3 to each data point, how many positive numbers would there be?

b = a + 3
print(b)

b_positives = (b > 0)
print(b_positives)
print(len(b_positives))

# 5. If you squared each number, what would the new mean and standard deviation be?

squared_array = a**2
print(squared_array)
print(mean(squared_array)) #74
print(stdev(squared_array)) #150.42

# 6. A common statistical operation on a dataset is centering. This means to adjust the data such that 
# the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data 
# set. See this link for more on centering.

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# we need to make the mean of the data 0, by subtracting the mean from each number in the array

centered_func = lambda x: x - x.mean() #build the function to accomplish the task
a_centered = centered_func(a) #create a new variable to store the output data
print(a_centered) #[  1.   7.   9.  20.  -5.  -4.  -3.  -3.  -3.  -9.   0. -10.] #produce the output

# 7. Calculate the z-score for each data point.

from scipy import stats

array_zscores = stats.zscore(a)
print(array_zscores)

# [  1.   7.   9.  20.  -5.  -4.  -3.  -3.  -3.  -9.   0. -10.] <<<<< array
# [ 0.12403473  0.86824314  1.11631261  2.48069469 -0.62017367 -0.49613894
#  -0.3721042  -0.3721042  -0.3721042  -1.11631261  0.         -1.24034735]


# 8. Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.