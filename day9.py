# day 9 code

# Numpy
# Numpy short for numerical python is a popular library used for scientific computing,numerical calculations and data analysis

# why use numpy
# fast array and matrix operations 
# used for n-dimensional array 
# statstics
# linear algebra
# random number operation


import numpy
# import numpy as np
# from numpy import arrange
# from numpy import *
n=numpy.arange(11)
print(type(n))
print(n)
print(n[0])


# example 2
import numpy
n=numpy.arange(12)
d=n.reshape(3,4)
print(type(d))
print(d)

# example 3
import numpy
n=numpy.arange(12).reshape(3,4)
print(n)

# example 4
import numpy
n=numpy.arange(36).reshape(3,4,3)
print(n)

# example 5 
import numpy
n=numpy.arange(12).reshape(3,4)
print(n)
print(n[0:4:,2])

# example 6
import numpy
n=numpy.arange(12).reshape(3,4)
print(n)
print(n[1:3,1])





