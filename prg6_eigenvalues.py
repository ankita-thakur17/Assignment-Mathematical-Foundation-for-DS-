 # Find all the eigenpairs of A
import numpy as np
from numpy.linalg import eig

#readig MatrixA file
CSVData = open("matrixA.csv")
A= np.loadtxt(CSVData,dtype="int", delimiter=",")
print("MATRIX A: ")
print(A)
print()
#finding eigen values and vector 
values,vectors=eig(A)
print('E-value:')
print(values)
print()
print('E-vector')
print(vectors)