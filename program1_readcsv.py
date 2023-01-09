#csv: common separated values
#reader and writer objects 

# file=open("file.csv",'w') CSV file opened in write mode 
#“w” will overwrite previous content
#“a” will add content to the end of previous content.

# file=open("file.csv",'r') CSV file opened in read mode 
#with: this statement will take care of any exception that may arise while opening/reading
#Read a matrix A from a csv file and a vector b from another csv file


import csv
import numpy as np
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