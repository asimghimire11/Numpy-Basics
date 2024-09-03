import numpy as np

arr0 = np.array(10)
print('0D Array')
print(type(arr0))
print(arr0)
print(arr0.ndim)

arr1 = np.array([10,20,50,48,75,63,21,25,235,2580])
print('1D array')
print(type(arr1))
print(arr1)
print(arr1.ndim)

arr2 = np.array([[10,20,30,40],[20,56,87,45]])
print('2D array')
print(type(arr2))
print(arr2)
print(arr2.ndim)

arr3 = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print('3D array')
print(type(arr3))
print(arr3)
print(arr3.ndim)