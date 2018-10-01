import numpy as np
import scipy
import sympy
from numpy import linalg as lg
from numpy.linalg import solve
from numpy.linalg import eig
from scipy.integrate import quad

# Question 1
# MC

# Question 2
# A.
'''
The statement is false. The matrix left bracket Start 1 By 1 Matrix 1st Row 1st Column Upper A Bold b 1 plus Upper A Bold b 2 plus Upper A Bold b 3 EndMatrix right bracket  is a 3 times 1 ​matrix, and AB must be a 3 times 3 matrix. The plus signs should be spaces between the 3 columns.
'''

# B.
'''
The statement is true. Let rowSubscript i​(A) denote the ith row of matrix A. Then rowSubscript i​(AB)equalsrowSubscript i​(A)B. Letting iequals2 verifies this statement. 
'''

# C
'''
The statement is false. The associative law of multiplication for matrices states that ​A(BC)equals​(AB)C.
'''

# D
'''
The statement is false. The transpose of the product of two matrices is the product of the transposes of the individual matrices in reverse​ order, or left parenthesis AB right parenthesis Superscript Upper TequalsUpper B Superscript Upper T Baseline Upper A Superscript Upper T. 
'''

# E
'''
The statement is true. This is a generalized statement that follows from the theorem left parenthesis Upper A plus Upper B right parenthesis Superscript Upper T Baseline equals Upper A Superscript Upper T Baseline plus Upper B Superscript Upper T.
'''

# Question 3
#A. 
# Answer: A.

#B.
# Answer: B.

# Question 4
# Invert the Matrix
M1 = np.array([[7, 3],
				[-16, -7]])
print(M1)
M1_inv = np.linalg.inv(M1)
print(M1_inv) # Correct, because determinant = 1

# The inverse of the matrix is the same as the matrix

# Question 5
'''

​Left-multiply each side of the equation ADequalsI by Upper A Superscript negative 1 to obtain Upper A Superscript negative 1ADequalsUpper A Superscript negative 1​I, IDequalsUpper A Superscript negative 1​, and DequalsUpper A Superscript negative 1.
'''

# Question 6
M2 = np.array([[1, 0, 4],
			  [-2, 1, 3],
			  [-3, -4, 3]])

print(M2)

M2_inv = np.linalg.inv(M2)
print(M2_inv) # Correct, but decimal not fraction, so the application wouldn't accept it

# Take 2
M3 = np.array([[1, 0, -2],
			   [4, 1, 2],
			   [3, -4, 2]])

print(M3)

M3_inv = np.linalg.inv(M3)
print(M3_inv)


# Question 7
# A. 
M4 = np.array([[1, 0, 0],
			   [2, 2, 0],
			   [3, 3, 3]])

print(M4)
M4_inv = np.linalg.inv(M4)
print(M4_inv)


# Question 8
# The matrix is not invertible because its determinant is zero.

# Question 9
'''
The matrix is invertible. The given matrix has three pivot positions.
'''

# Question 10
'''
A. 
True; by the Invertible Matrix​ Theorem, if there is an n times n matrix D such that ADequals​I, then it must be true that there is also an n times n matrix C such that CAequalsI.
This is the correct answer.C.

B. 

​True; by the Invertible Matrix Theorem if the columns of A are linearly​ independent, then the columns of A must span set of real numbers R Superscript n.

C. 

​True; by the Invertible Matrix Theorem if Axequalsb has at least one solution for each b in set of real numbers R Superscript n​, then matrix A is invertible. If A is​ invertible, then according to the invertible matrix theorem the solution is unique for each b.

D. 


​False; the linear transformation ​(x​) maps to Ax will always map set of real numbers R Superscript n into set of real numbers R Superscript n for any n times n matrix. According to the Invertible Matrix Theorem A has n pivot positions only if left parenthesis Bold x right parenthesis maps to Upper A Bold x maps set of real numbers R Superscript n onto set of real numbers R Superscript n.

E. 

True; according to the Invertible Matrix Theorem if there is a b in set of real numbers R Superscript n such that the equation Axequalsb is​ inconsistent, then equation Axequalsb does not have at least one solution for each b in set of real numbers R Superscript n and this makes A not invertible.

'''

# Question 11
'''

If the columns of A are linearly independent and A is​ square, then A is​ invertible, by the IMT.​ Thus, Asquared​, which is the product of invertible​ matrices, is also invertible.​ So, by the​ IMT, the columns of Asquared span set of real numbers R Superscript n.
'''

# Question 12
'''
Let W be the inverse of AB. Then WABequalsI and ​(WA)BequalsI. ​Therefore, matrix B is invertible by part​ (j) of the IMT.
'''
