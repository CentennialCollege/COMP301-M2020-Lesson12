import numpy as np

matrix2 = []
colCount = 0

for row in range(4):
    matrix2.append(np.arange(1 + colCount, 5 + colCount))
    colCount += 4

matrix2 = np.array(matrix2)

print(matrix2)

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

#print(matrix)

multi = np.array(matrix)

#print(multi)

#print(multi.dtype)

#print(multi.ndim)

#print(multi.shape)

#for row in multi.flat:
#    print(row, end=' ')


matrix3 = np.arange(1, 17).reshape(4, 4)

print(matrix3)

matrix4 = np.arange(1, 16).reshape(3, 5)

print(matrix4)

print(matrix4.mean(axis=1))