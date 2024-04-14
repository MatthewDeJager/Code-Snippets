



rows1 = int(input('Number of rows of matrix 1:    '))
columns1 = int(input('Number of columns of matrix 1: '))
order1 = (rows1, columns1)
rows2 = int(input('Number of rows of matrix 2: '))
columns2 = int(input('Number of columns of matrix 2: '))
order2 = (rows2, columns2)
print('')
print(order1)
print(order2)
print('')
if order1[1] == order2[0]:
  print('Matrix multiplication is possible')
else:
  print('Matrix multiplication is not possible')
matrix1 = []

for i in range(order1[0]):
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
for i in range(order2[0]):
  row = []
  for j in range(order2[1]):
     element = int(input(f'Element in row {i+1} and column {j+1} of matrix 2: '))
     row.append(element)
  matrix2.append(row)
print('\nMatrix2: ')
for x in range(order2[0]):
   print(f'{matrix2[x]}')















#multiply
def multiply(matrix1, matrix2, orderM1, orderM2):
  order1 = tuple(orderM1)
  order2 = tuple(orderM2)
  elementNew = []
  newMatrix = []
  sum = 0
  for j in range(order1[0]):
    for x in range(order1[0]):
      for i in range(order1[1]):
        sum += matrix1[j][i]*matrix2[i][x]
      elementNew.append(sum)
      sum = 0
    newMatrix.append(elementNew)
    elementNew = []
  return newMatrix


newMatrix = multiply(matrix1, matrix2, order1, order2)

print(f"\n\n\nMultiplied matrix: \n")

for element in newMatrix:
  print(element)




