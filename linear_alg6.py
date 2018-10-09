import numpy as np
import scipy
import sympy
from numpy import linalg as lg
from numpy.linalg import solve
from numpy.linalg import eig
from scipy.integrate import quad

# Question 1
'''
If uequalsStart 2 By 1 Table 1st Row 1st Column x 2nd Row 1st Column y EndTable 			  is in​ W, then the vector cuequalscStart 2 By 1 Table 1st Row 1st Column x 2nd Row 1st Column y EndTable 			 equalsStart 2 By 1 Table 1st Row 1st Column cx 2nd Row 1st Column cy EndTable 			  is in W because left parenthesis cx right parenthesis left parenthesis cy right parenthesisequalsc squared left parenthesis xy right parenthesis less than or equals 0 since xy less than or equals 0.

Part B

[0 2]
[2 0]
'''

# Question 2
'''
The set is a subspace of set of prime numbers P 5. The set contains the zero vector of set of prime numbers P 5​, the set is closed under vector​ addition, and the set is closed under multiplication by scalars.
'''

# Question 3

'''
A.
The coefficients form the vectors.

B.
W = Span{U,V}

C.
Since u and v are in set of real numbers R Superscript 4 and WequalsSpan StartSet Bold u comma Bold v EndSet​, W is a subspace of set of real numbers R Superscript 4.
'''


# Question 4
'''
W is not a vector space because the zero vector and most sums and scalar multiples of vectors in W are not in​ W, because their second​ (middle) value is not equal to negative 3.
'''

# Question 5
'''
No, because:

Aw = [14]
	 [14]
	 [ 3]
'''

# Question 6
'''
Spanning set for Nul A is:

[-3] [0]
[ 1] [0]
[ 0] [0]
[ 0] [1]

# Question 7
'''
# The set W is a subset of set of real numbers R Superscript 4. If W were a vector​ space, what else would be true about​ it? 

#A. 
#The set W would be a subspace of set of real numbers R Superscript 4.

#B. 
#The zero vector is not in W. There is no t and s such that the vector equation is satisfied.

#C.
#Since the zero vector is not in​ W, W is not a subspace of set of real numbers R Superscript 4. Thus W is not a vector space.
'''

# Question 8

# A.
# k = 3

# B. 
# k = 2
'''
# Question 9
mat = sympy.Matrix([[9, 3], [3, 1], [-12, -4], [6,2]])
print(mat)
print(mat.rref())

# Nonzero vector in Nul A is:
'''
[ 1]
[-3]

Nonzero vector in Col A is:
[  9]
[  3]
[-12]
[  6]
'''

# Question 10
'''
The set spans set of real numbers R cubed.

The set is linearly independent.

The set is a basis for set of real numbers R cubed.
'''

# Question 11

mat2 = sympy.Matrix([[1, 1, -1, -1, 2, 0], [0, 1, 0, -2, -3, 0], [0, 0, -8, 0, 16, 0]])

print(mat2)
print(mat2.rref())

# The rref represents the equations:
'''
x1 + 0 + 0 x4 + 3x5 = 0
0  +x2 + 0-2x4- 3x5 = 0
0  + 0 +x3 + 0 -2x5 = 0

[x1] = -x4 - 3x5
[x2] = 2x4 + 3x5
[x3] = 2x5
[x4] = x4
[x5] = x5

	[-1]
	[ 2]
x4  [ 0]
	[ 1]
	[ 0]


	[-3]
	[ 3]
x5  [ 2]
	[ 0]
	[ 1]
# Correct
'''

# Question 12
'''
A.
The statement is false because the subspace spanned by the set must also coincide withnbspH.

B.
The statement is true by the Spanning Set Theorem.

C.
The statement is true by the definition of a basis.

D.
The statement is false because the method always produces an independent set.\

E. 

The statement is false because the columns of an echelon form B of A are not necessarily in the column space of A.
'''

# Question 13
'''
	[-4]
x =  [4]
	[-8]
'''

# Question 14
mat3 = sympy.Matrix([[1, 3, 1, -1], [-1, -2, -1, 0], [-2, -6, 5, 9]])

print(mat3)

print(mat3.rref())

# Question 15
# Form a matrix from the two vectors. It is identical.