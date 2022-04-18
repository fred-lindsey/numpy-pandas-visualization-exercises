from statistics import mean, stdev
import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?

a[a < 0].size ## Vectorized operations
print(a[a < 0].size) ## 4

# 2. How many positive numbers are there?

a[a > 0] ## adding '.size' will give the number of values produced by the operation
print(a[a > 0])
#print(f'a array positive numbers == {a >= 0}')

# .size v .shape v len
# size returns all items in array
# shape returns the dimensions of the array
# len reutrns the number of elements contianed only in the outer-most array

# 3. How many even positive numbers are there?

a[(a > 0) & (a % 2 ==0)]
print(a[(a > 0) & (a % 2 ==0)])
#print(f'a array even positive numbers == {a >= 0 & a % 2 == 0}')

# 4. If you were to add 3 to each data point, how many positive numbers would there be?

b = a + 3
print(b)

b_positives = b[(b > 0)] #this will print the values of b, where b is positive. the inner clause will only return T/F (boolean mask)
print(f'b_positives equals {b_positives} ')
print(len(b_positives)) ## or print(b_positives.size())
print(b_positives.size)

# 5. If you squared each number, what would the new mean and standard deviation be?

squared_array = a**2
print(squared_array)
print(mean(squared_array)) #74
print(stdev(squared_array)) #150.42

# 6. A common statistical operation on a dataset is centering. This means to adjust the data such that 
# the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data 
# set. See this link for more on centering.

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
print(f'{a} is the orginal array')

# we need to make the mean of the data 0, by subtracting the mean from each number in the array

centered_func = lambda x: x - x.mean() #build the function to accomplish the task
a_centered = centered_func(a) #create a new variable to store the output data
print(a_centered) #[  1.   7.   9.  20.  -5.  -4.  -3.  -3.  -3.  -9.   0. -10.] #produce the output

# 7. Calculate the z-score for each data point.

from scipy import stats

#a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

array_zscores = stats.zscore(a)
print(array_zscores)

# OR

array_zscores = (a - a.mean())/ a.std()
print(array_zscores)

# [  1.   7.   9.  20.  -5.  -4.  -3.  -3.  -3.  -9.   0. -10.] <<<<< array
# [ 0.12403473  0.86824314  1.11631261  2.48069469 -0.62017367 -0.49613894
#  -0.3721042  -0.3721042  -0.3721042  -1.11631261  0.         -1.24034735]

# _________________________________________________________________________________________________________________ /*
# 8. Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.
import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

sum_of_a = sum(a)
print(sum(a)) #55

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = min(a)
print(min(a)) #1

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
print(max(a)) #10

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = sum(a)/len(a)
print(mean_of_a) #5.5


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = a[0] # create a list that begins at the 0 index for array a. this will
#be the basis for the multiplier

for i in a[1:]: #create a variable in a to iterate through a
    print(f' current value of {product_of_a} ') #check your initial values
    print(f' current value of {i} ')
    product_of_a *= i      #p = p * i, overwriting what's stored there. set a multiplier
    #to iterate through the list and receive the values
    print(f' after value of {product_of_a} ')


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

squares_of_a = [i*i for i in a]
print(squares_of_a)

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

odds_in_a = [i for i in a if i % 2 != 0]
print(odds_in_a)

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = [i for i in a if i % 2 == 0]
print (evens_in_a)

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.

b = [
    [3, 4, 5],
    [6, 7, 8]
]

b = np.array ([
    [3, 4, 5],
    [6, 7, 8]
])

print(b)

print(b.min()) #min is a method for a NumPy array >> 3

print(b.mean()) # >> 5.5

print(b.sum()) # >> 33

print(b.prod()) # >> 20160

print(np.square(b)) # >> [[ 9 16 25]
 #                      [36 49 64]]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
# sum_of_b = 0
# for row in b:
#     sum_of_b += sum(row)

sum_of_b = np.sum(b[0])
print(sum_of_b) #12

# Exercise 2 - refactor the following to use numpy. 
# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

min_of_b = b.min()
print(min_of_b) # >> 3



# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
max_of_b = np.max(b)
print(max_of_b) ## >> 8




# Exercise 4 - refactor the following using numpy to find the mean of b
#mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

mean_of_b = np.mean(b)
print(mean_of_b) ## 5.5


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

# Exercise 6 - refactor the following to use numpy to find the list of squares 
# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)

# squares_of_b = np.square[b]
# print(f' {squares_of_b} are the squares_of_b' )


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

# Exercise 9 - print out the shape of the array b.

array_b_shape = np.shape(b)
print(array_b_shape) # (2, 3) 2 col, 3 rows

# Exercise 10 - transpose the array b.

print(b.T) ## rows become the new columns


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

print(b.flatten()) ## produces a single list of 6 numbers

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

print(b.reshape(6, 1))

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

c = np.array ([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

 #transform into NumPy array

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
print(c.min())
print(c.max())
print(c.prod())

# Exercise 2 - Determine the standard deviation of c.
c.std()
# Exercise 3 - Determine the variance of c.
c.var()
# Exercise 4 - Print out the shape of the array c
print(c.shape)
# Exercise 5 - Transpose c and print out transposed result.
np.transpose(c) 
# Exercise 6 - Get the dot product of the array c with c. 
np.dot(c, c)
# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
#print(c * c.T).sum()
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.


## Setup 4
d = np.array ([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
])

print(d)

# Exercise 1 - Find the sine of all the numbers in d

np.sin(d)

# Exercise 2 - Find the cosine of all the numbers in d

np.cos(d)

# Exercise 3 - Find the tangent of all the numbers in d
np.tan(d)
# Exercise 4 - Find all the negative numbers in d
d[d<0]
# Exercise 5 - Find all the positive numbers in d
d[d>0]
# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d)
# Exercise 7 - Determine how many unique numbers there are in d.
np.unique(d).size
# Exercise 8 - Print out the shape of d.
d.shape
# Exercise 9 - Transpose and then print out the shape of d.
d.T.shape 
# Exercise 10 - Reshape d into an array of 9 x 2
d.reshape(9, 2)