#Solve the equation Ax=b and check whether there are 0,1 or infinitely many solutions
import numpy as np
import csv
from scipy import linalg

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
print()

#finding possible solution i.e. uique, finite or infinite solution
print("Solution:")
result=np.linalg.solve(A, B)
print(result)
print()
