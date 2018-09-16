import numpy as np
from numpy import linalg as lg
from numpy.linalg import solve
from numpy.linalg import eig
from scipy.integrate import quad

# Question 1
# MC question
# Part a. C. Not defined because the columns don't match the # of entries
# Part b. C.

# Question 2
# Write the system as a vector equation and then as a matrix equation
'''
8x1 + x2 - 3x3 = 8
     2x2 + 3x3 = 0

# Vector Equation

x1 8 + x2 1 + x3 -3 = 8
   0      2       3   0

# Matrix equation

		  [x1]
[8 1 -3]  [x2] = [8]
[0 2  3]  [x3]   [0]

'''

# Question 3
# Part a builds an augmented matrix

# Part b, Solve:

a = np.array([[1, 4, -3], [-3, -5, 2], [4, 2, 6]])
b = np.array([[-1, 17, -20]])

print(a, '\n\n', b.T, '\n')

x = np.linalg.solve(a, b.T)
print(x) # Correct


