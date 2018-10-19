import numpy as np
import scipy
import sympy
from numpy import linalg as lg
from numpy.linalg import solve
from numpy.linalg import eig
from scipy.integrate import quad

# Question 1
'''

		[1][-8]
basis = [1][ 1]
		[0][ 2]

The dimension is 2.
'''

#Question 2
'''
The dimension is 2 (number of pivot columns in the matrix)
'''

# Question 3
'''
The dimension of Nul A is 3, the dimension of Col A is 2.
'''

# Question 4
'''
The dimension of Nul A is 0, the dimension of Col A is 3.
'''

# Question 5
'''
Let B be the basis of set of prime numbers P 3 consisting of the Hermite polynomials​ 1, 2t, negative 2 plus 4 t squared comma and negative 12 t plus 8 t cubed ; and let Bold p left parenthesis t right parenthesis equals 10 minus 4 t squared plus 8 t cubed . Find the coordinate vector of p relative to B.
'''

mat = sympy.Matrix([[1, 0, -2, 0, 10], [0, 2, 0, -12, 0], [0, 0, 4, 0, -4], [0, 0, 0, 8, 8]])

print(mat)
rref = mat.rref()

print(rref) # Correct

# Question 6


# Question 7


# Question 8
'''
dim Row A = 3
'''

# Question 9
mat1 = np.array([[6, -1, 1], [0, 2, 1], [-2, 0, 4]])
print(mat1)
arr1 = np.array([[1, -2, 2]])
print(arr1)

#Answer:
# 10
#-2
# 6

# Question 10
mat2 = sympy.Matrix([[1, 1, -7, 3], [4, 3, -16, 7]])
print(mat2.rref()) # correct

# Question 11
'''
The statement is true. The columns of ModifyingBelow Upper P With Upper C left arrow Upper B are linearly independent because they are the coordinate vectors of the linearly independent set B.

The statement is false. Matrix P satisfies left bracket Bold x right bracket Subscript Upper C Baseline equals Upper P left bracket Bold x right bracket Subscript Upper B for all x in V.
'''

# Question 12
mat3 = sympy.Matrix([[1, 3, 0, -1], [-2, -5, 2, 2], [1, 4, 3, 0]])
print(mat3)

rref1 = mat3.rref()
print(rref1)