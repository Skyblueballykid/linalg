import numpy as np
import scipy
import sympy
from numpy import linalg as lg
from numpy.linalg import solve
from numpy.linalg import eig
from scipy.integrate import quad

# Question 1

# The Eigenvalue is 6

# Question 2

# v is not an eigenvector of A

# Question 3

'''
A.
The basis is: 
[ 0]
[-4]

B.
The basis is:
[4]
[4]
'''

# Question 4
'''
a. 
False. The condition that Axequalslambdax for some scalar lambda is not sufficient to determine if x is an eigenvector of A. The vector x must be nonzero.

b.
False. There may be linearly independent eigenvectors that both correspond to the same eigenvalue.

c.
True. A​ steady-state vector for a stochastic matrix is actually an eigenvector because it satisfies the equation Axequalsx.

d.
False. If the matrix is a triangular​ matrix, the values on the main diagonal are eigenvalues.​ Otherwise, the main diagonal may or may not contain eigenvalues.

e.
True. An eigenspace of A corresponding to the eigenvalue lambda is the null space of the matrix ​(Aminuslambda​I).
'''

# Question 5
'''
Attempt 1
AD = 
FOIL:
(-3 - lambda)(-1 - lambda)
lambda ^2 + 4lambda + 3

AD - BC:
Characteristic polynomial:
lambda ^2 + 4lambda + 1

Set the characteristic polynomial equal to 0 and solve to find the eigenvalues:
lambda ^2 + 4lambda + 1 = 0

Attempt 2
Foil AD = 
(5 - lambda)(-1 - lambda)
lambda ^2 - 4 lambda - 5

AD - BC:
lambda ^2 - 4 lambda - 3

Use the quadratic equation to find the roots:
2 + sqrt(7), 2 - sqrt(7)
'''

# Question 6
'''
D1 = (1 - lambda)(2 - lambda)(-lambda)
D2 = 0
D3 = -21

U1 = 0
U2 = -14(1 - lambda)
U3 = 0

D1 + D2 + D3 - U1 - U2 - U3 
(1 - lambda)(2 - lambda)(-lambda) + 0 +(-21) - 0 - (-14(1 - lambda)) - 0

(1 - lambda)(2 - lambda)(-lambda) - 21 + 14 - 14lambda
(2 - lambda - 2lambda + lambda^2)(-lambda) - 14lambda - 7
-lambda^3 +3lambda^2- 16lambda -7 # Correct
'''

# Question 7
# The real eigenvalues are just the coefficients of the diagonal
# 0, 2, 2, 9, 9

# Question 8
# Attempt 1
'''
pinv = np.array([[-5, 3],[2, -1]])
print(pinv)

p = np.linalg.inv(pinv)
print(p)

d = np.array([[1,0],[0,3]])
d4 = d ** 4
print(d4)

#Multiply p and D^4
pd4 = np.array([[1,3],[2,405]])
print(pd4)

# Multiply by pinv
final = pd4 * pinv
print(final)
'''

# Attempt 2
p = np.array([[1,2],[3,5]])
print(p)

pinv = np.linalg.inv(p)
print(pinv)

d = np.array([[1,0],[0,2]])
print(d)

d4 = d ** 4
print(d4)

mult = np.dot(p, d4)
print(mult)

a4 = np.dot(mult, pinv)
print(a4) # Correct


# Question 9
'''
p = np.array([[7,0],[3,1]])
'''

# Question 10
# The matrix is just the coefficients

# Question 11
# Attempt 1
# First find the eigenvalues
# Foil:
'''
(-1 - lambda)(6 - lambda) - (-12)
lambda^2 - 5lambda - 18

# Attempt 2
(6 - lambda) (1 - lambda) - (-6)
lambda^2 - 7lambda + 12

Factor:
(lambda - 3)(lambda -4)

# The second vector is the inverse of the bd diagonal
B = np.array([[1, -1], [-3, 2]])

# This is the answer from factoring the polynomial
TB = np.array([[3, 0], [0,4]])
