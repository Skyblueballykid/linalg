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
mat = np.array([[1,1,0], [3, 0, 5], [0, 1, -5]])
print(mat)
det8 = np.linalg.det(mat)
print(det8)

#Cramer's Rule
# Find A1b by replacing the first column with column b
mat2 = np.array([[2,1,0], [0, 0, 5], [3, 1, -5]])
print(mat2)
det9 = np.linalg.det(mat2)
print(det9)
print(det9/det8)

#Find A2b by replacing the second column with b
mat3 = np.array([[1, 2, 0], [3, 0, 5], [0, 3, -5]])
print(mat3)
det10 = np.linalg.det(mat3)
print(det10)
print(det10/det8)

#Find A3b by replacing the third column with b
mat4 = np.array([[1, 1, 2], [3, 0, 0], [0, 1, 3]])
print(mat4)
det11 = np.linalg.det(mat4)
print(det11)
print(det11/det8)

# Answers above are correct, but try again because I misread the print output

matr = np.array([[1,1,0], [5, 0, 4], [0, 1, -4]])
print(matr)
deter = np.linalg.det(matr)
print(deter)

# Find A1b by replacing first column with b
matr1 = np.array([[5, 1, 0], [0, 0, 4], [6, 1, -4]])
print(matr1)
deter1 = np.linalg.det(matr1)
print(deter1/deter)

# Find A2b by replacing second column with b
matr2 = np.array([[1, 5, 0], [5, 0, 4], [0, 6, -4]])
print(matr2)
deter2 = np.linalg.det(matr2)
print(deter2/deter)

# Find A3b by replacing third column with b
matr3 = np.array([[1, 1, 5], [5, 0, 0], [0, 1, 6]])
print(matr3)
deter3 = np.linalg.det(matr3)
print(deter3/deter)

# Question 13
# Compute the adjugate of the given matrix
matri = np.matrix([[2, 5, 4], [1, 0, 1], [3, 2, 2]])
print(matri)
# Hermitian transpose (not correct)
print(matri.getH())
# Det of matrix
determ = np.linalg.det(matri)
print(determ)

adj_matr = np.array([[-2, -2, 5], [1, -8, 2], [2, 11, -5]])
print(adj_matr * 1/determ) # Correct

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
