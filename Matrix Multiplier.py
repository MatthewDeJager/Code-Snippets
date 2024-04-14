#Matrix Multiplier

import sys

#Function for multiplying matrices
def multiply(matrix1, matrix2, orderM1, orderM2):
  order1 = tuple(orderM1)
  order2 = tuple(orderM2)
  elementNew = []
  newMatrix = []
  sum = 0

  #iterates over the necessary values in the matrix to multiply them.
  #j variable represents the amount of rows: it iterates downwards
  #i variable represents the amount of columns: it iterates sideways
  #x variable is used to iterate downwards

  for j in range(order1[0]): # iterates to create a list for each row
      for x in range(order1[0]):# iterates to ensure the calculation of the different values in each row and creates a list for the row
        for i in range(order1[1]): # calculates the individual values in the matrix in each column
          sum += matrix1[j][i]*matrix2[i][x]
        elementNew.append(sum)
        sum = 0
      newMatrix.append(elementNew)
      elementNew = []

  return newMatrix
  #end of function


#Inputs the rows and columns of the matrices to be input
print("\n")
rows1 = int(input('Number of rows of matrix 1:    '))
columns1 = int(input('Number of columns of matrix 1: '))
order1 = (rows1, columns1)
rows2 = int(input('Number of rows of matrix 2:    '))
columns2 = int(input('Number of columns of matrix 2: '))
order2 = (rows2, columns2)

#Calculates if matrix multiplication is possible
if order1[1] == order2[0]:

    print('')
    print("Order of matrix1: ",order1)
    print("Order of matrix2: ",order2)
    print('')

    matrix1 = []

    for i in range(order1[0]): #Inputs first matrix
        row = []
        for j in range(order1[1]):
            element = int(input(f'Element in row {i+1} and column {j+1} of matrix1: '))
            row.append(element)
        matrix1.append(row)
    print(f'\nMatrix 1:')
    for x in range(order1[0]):
        print(matrix1[x])
    print('')

    matrix2 = []

    for i in range(order2[0]): #Inputs second matrix
        row = []
        for j in range(order2[1]):
            element = int(input(f'Element in row {i+1} and column {j+1} of matrix 2: '))
            row.append(element)
        matrix2.append(row)
    print('\nMatrix2: ')
    for x in range(order2[0]):
        print(f'{matrix2[x]}')
else:
    sys.exit("\n\nMatrices are not compatible for multiplication.\nMatrix multiplication is not possible as the number of rows in the one matrix does not equal the number of columns in the other matrix.\n\n")

#Creates resulting matrix by calling the multiply function
newMatrix = multiply(matrix1, matrix2, order1, order2)

print(f"\n\nResulting matrix: \n")

for element in newMatrix: #Prints resulting function
  print(element)
print("\n")













