#. Perform LU decomposition for square matrix using NumPy or SciPy libraries
import numpy as np
import csv
import scipy.linalg
#readig MatrixA file
CSVData = open("matrixA.csv")
A= np.loadtxt(CSVData,dtype="int", delimiter=",")
print("MATRIX A: ")
print(A)
print()
#reading VectorB file
CSVData1 = open("vectorB.csv")
B= np.loadtxt(CSVData1,dtype="int", delimiter=",")
print("VECTOR B: ")
print(B)
B.shape=(3,1)
print()

#LU decomposition
P,L,U=scipy.linalg.lu(A)

#print Input Matrix A
print("Input Matrix")
print(A)
print()
print("Permutation matrix")
print(P)
print()
print("Lower triangular matrix")
print(L)
print()
print("Upper triangular matrix")
print(U)
print()
#multiply them and check if we get the original matrix A back
print("Final Output Matrix")
result=P.dot((L.dot(U)))
print(result)
print()





