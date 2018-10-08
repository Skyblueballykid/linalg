import numpy as np
import scipy
import sympy
from numpy import linalg as lg
from numpy.linalg import solve
from numpy.linalg import eig
from scipy.integrate import quad

# Question 2

m1 = np.array([[4, -1, -1, 0], [-1, 4, 0, -1], [-1, 0, 4, -1], [0, -1, -1, 4]])
print(m1)

det = np.linalg.det(m1)
print(det)

# Question 5
m2 = np.array([[20, -1, -1, 0], [50, 4, 0 ,-1], [15, 0, 4, -1], [45, -1, -1, 4]])
print(m2)
det2 = np.linalg.det(m2)
print(det2)

#x1
print(det2/det)
