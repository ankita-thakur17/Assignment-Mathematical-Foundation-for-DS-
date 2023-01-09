 # Do the diagonalization of a matrix (assume it is symmetric)
import numpy as np
import csv
from numpy.linalg import eig
import scipy
#Symmetric Matrix
A=np.matrix([[2,3,6],[3,4,5],[6,5,9]])
print("Input Symmetric Matrix: ")
print(A)
print()

print("Diagonalisation of A: ")
values=eig(A) # eigen values and vectors 
D = np.diag(values[0]) # diagonalisation of A from its eigen values
print(D)
print()

#P=values[1]   # such as A = P.D.P(-1) 
#np.linalg.inv(P)
#print(P)