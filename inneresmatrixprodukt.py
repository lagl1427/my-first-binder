import numpy as np

#arr = np.random.randn(6, 3)
#arr = np.arange(3,3)
arr = np.arange(9).reshape((3, 3))

print (arr)

# Matrizenmultiplikation
print(np.dot(arr, arr))

#Transpose
print(arr.T)

# Transpose Multiplication
print(np.dot(arr.T, arr))

# Ufunc
arr2 = np.random.randn(7) * 5
print(arr2)
print(np.modf(arr2))
