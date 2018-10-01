import numpy as np
import scipy
import sympy
from numpy import linalg as lg
from numpy.linalg import solve
from numpy.linalg import eig
from scipy.integrate import quad


# Question 1
'''
A. Determinant = -21

B. Determinant = -21

'''

m1 = np.array([[3, 0, 3], [2, 3, 3], [0, 4, -1]])
print(m1)

det1 = np.linalg.det(m1)
print(det1) # correct

# Question 2
# Det = -159

# Question 3
'''
A. 
Replace row 3 with k times row 3.

B. 
The determinant is multiplied by k.
'''

# Question 4
m2 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
det2 = np.linalg.det(m2)
print(det2) # correct

# Question 5
'''
A.
False, because the determinant of A can be computed by cofactor expansion across any row or down any column. Since the determinant of A is well​ defined, both of these cofactor expansions will be equal.

B.

​False, because the determinant of a triangular matrix is the product of the entries along the main diagonal.
'''

# Question 6
'''
If two rows of A are interchanged to produce​ B, then det Upper B equals negative det A.
'''

# Question 7
'''
If a multiple of one row of A is added to another row to produce matrix​ B, then det Upper B equals det Upper A.
'''

# Question 8
m3 = sympy.Matrix([[1, 5, -6], [-1, -4, -5], [1, 4, 7]])
print(m3)
rref1 = m3.rref()
print(rref1)

m4 = np.array([[1, 5, -6], [-1, -4, -5], [1, 4, 7]])
det3 = np.linalg.det(m4)
print(det3) # correct, det = 2

# Question 9
# Switch the rows, det of original matrix = -10, det of changed matrix = 10

# Question 10
m5 = np.array([[-25, -4, -2], [-5, 12, -4], [0, -20, 6]])
det4 = np.linalg.det(m5)
print(det4)
# The matrix is invertible because the determinant of the matrix is not zero.

# Question 11
# formula

# Question 12


# Question 13


# Question 14
m6 = np.array([[3, 7], [6, 2]])
print(m6)
det5 = np.linalg.det(m6)
print(det5) # correct
# The area of the parellelogram is the absolute value of the det. In this case = 36

# Question 15
# First find the area of the parellelogram
m7 = np.array([[-5, -5], [5, 10]])
det6 = np.linalg.det(m7)
print(det6) # -25

# next find the det of matrix A
m8 = np.array([[7, -8], [-2, 8]])
print(m8)
det7 = np.linalg.det(m8)
print(det7) # 40

# Finally, multiply the absolute value of the det of the first matrix (area of the parellelogram) by the det of the second matrix 
# Answer = 1000
