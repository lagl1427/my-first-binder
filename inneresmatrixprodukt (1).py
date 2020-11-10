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

#Meshgrid
points = np.arange(-5, 5, 1) # 1000 equally spaced points
print(points)
xs, ys = np.meshgrid(points, points)

print("xs", xs)
print("ys", ys)

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
print("Zip:", zip(xarr, yarr, cond))
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
print("ResultZIPIf", result)

#besser
result = np.where(cond, xarr, yarr)
print("ResultZIPIf", result)