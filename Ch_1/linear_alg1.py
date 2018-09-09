import numpy as np
from numpy import linalg as lg
from numpy.linalg import solve
from numpy.linalg import eig
from scipy.integrate import quad

# MAT 350 - Linear Algebra
# Homework 1

# Question 1
'''
x^1 + 2x^2 = 8
x^1 - x^2 = 2

[1 2 | 8]
[1 -1 | 2]

x1 = 4
x2 = 2
'''

# Question 2
'''
x^2 + 3x^3 = 3
x^1 + 2x^2 + 2x^3 = -5
5x^1 + 9x^2 + 7x^3 = 2

Matrix:
[0 1 3 | 3]
[1 2 2 | -5]
[5 9 7 | 2]

Interchange rows 1 & 2:
[1 2 2 | -5]
[0 1 3 | 3]
[5 9 7 | 2]

Row operation to change entry in 3rd row, column 1 to a 0:
(subtract 5 * row 1)
[1 2 2 | -5]
[0 1 3 | 3]
[0 -1 -3 | -23]

Add row 2 to row 3 to zero out the left side of row 3:
[1 2 2 | -5]
[0 1 3 | 3]
[0 0 0 | -20]

This problem has no solution because the 3rd row is the inequality:
0 = 20
'''

# Question 3
'''
[1 h 4]
[5 10 16]

Subtract 5 * row 1 from row 2:
[1 h 4]
[0 10 - 5h | -4]

Rewrite as a system of linear equations:
x^1 + hx^2 = 4
(10 - 5h)x^2 = -4

If h = 2, the equation is undefined, so h != 2
'''


# Question 4
# Multiple Choice

# Question 5
# Multiple Choice


