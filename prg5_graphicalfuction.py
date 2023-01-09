import numpy as np
import matplotlib.pyplot as plt

#readig MatrixA file
CSVData = open("matrixA.csv")
A= np.loadtxt(CSVData,dtype="int", delimiter=",")
print("MATRIX A: ")
print(A)
print()

#exponential function
print("NumPy Exponential Functions")
print(np.exp(A))
print()

#sine function
print("NumPy Trigonometric Sine Functions")
print(np.sin(A * np.pi / 180))
print()
#sigmoid function
print("NumPy Sigmoid Functions")
print(1/(1 + np.exp(-A)))
print()