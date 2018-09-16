import numpy as np
import scipy
import sympy
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

a1 = np.array([[1, 4, -3], [-3, -5, 2], [4, 2, 6]])
b1 = np.array([[-1, 17, -20]])

print(a1, '\n\n', b1.T, '\n')

x1 = np.linalg.solve(a1, b1.T)
print(x1, '\n') # Correct


# Question 4 
# MC question
# Answer: D. Yes. When the given vectors are written as the columns of a # matrix​ A, A has a pivot position in every row.


# Question 5
# The coefficients of the equation are the answer
# Answer:
# X1 = -4
# X2 = -4

# Question 6
# Multiple Choice
# Part A
# Could a set of three vectors in set of real numbers R4 span all of set of real numbers R4​?
# No. The matrix A whose columns are the three vectors has four rows. To have # a pivot in each​ row, A would have to have at least four columns​ (one for # each​ pivot.)

# Part B
# Could a set of n vectors in set of real numbers Rm span all of set of real # numbers Rm when n is less than​ m? Explain. Choose the correct answer
# No. The matrix A whose columns are the n vectors has m rows. To have a pivot # in each​ row, A would have to have at least m columns​ (one for each​ pivot.) 


# Question 7
# The system has a nontrivial solution

# Question 8
a2 = np.array([[4, 4, 8], [-8, -8, -16], [0, -3, 9], [0, 0, 0]])
b2 = np.array([[0, 0, 0]])

c1 = sympy.Matrix(a2).rref()
print("The Matrix in RREF is: ", c1)

# Simplifies to:
'''
x1 +    5x3 = 0
    x2 -3x3 = 0
          0 = 0

x1 = -5x3
x2 =  3x3

    x1   -5x3   -5
x = x2 =  3x3 =  3
    x3     x3    1

x = x3[-5, 3, 1]
'''


# Question 9


# Question 10
# Part A
# A is a 3x3 matrix with 3 pivot positions
# Does the equation Ax = 0 have a nontrivial solution?
# Answer: No

# Part B
# Does the equation Axequalsb have at least one solution for every possible b​?
# Answer: Yes
'''
With three pivot​ positions, A has a pivot position in each of its three​ rows, and​ therefore, for each b in set of real numbers R cubed​, the equation Axequalsb has a solution.'''

