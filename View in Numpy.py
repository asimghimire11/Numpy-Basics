import numpy as np
arr1 = np.arange(1,11,1)
print(arr1)
print('Address of original array :',id(arr1))
arv = arr1.view()
print(arv)
print('Address of view:', id(arv))
arr1[3] = 500 #View creates a mirror image of the original array, so any changes in original or view array will reflect in both arrays
arv[5] = 800
print('After Change: ')
print(arr1)
print(arv)