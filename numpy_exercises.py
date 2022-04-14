import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?

a[a < 0]

# 2. How many positive numbers are there?

a[a > 0]

#print(f'a array positive numbers == {a >= 0}')

# 3. How many even positive numbers are there?

a[(a > 0) & (a % 2 ==0)]

#print(f'a array even positive numbers == {a >= 0 & a % 2 == 0}')

# 4. If you were to add 3 to each data point, how many positive numbers would there be?



# 5. If you squared each number, what would the new mean and standard deviation be?
# 6. A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.
# 7. Calculate the z-score for each data point.
# 8. Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.