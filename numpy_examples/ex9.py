# Python code to demonstrate matrix operations
# multiply() and dot()

# importing numpy for matrix operations
import numpy

# initializing matrices
x = numpy.array([[1, 2], [4, 5]])
y = numpy.array([[7, 8], [9, 10]])
print(x)
print(y)

# using multiply() to multiply matrices element wise
print("The element wise multiplication of matrix is : ")
print(numpy.multiply(x, y))

# using dot() to multiply matrices
print("The product of matrices is : ")
print(numpy.dot(x, y))

# EOF
