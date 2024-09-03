import numpy as np
arr1 = np.arange(1,11,1)
print(arr1)
print('Address of original array :',id(arr1))
arc = arr1.copy()
print(arc)
print('Address of Copy :',id(arc))
arr1[3] = 500#in copy changes in either array doesnot reflect to other array
arc[5] = 800
print('After Changes: ')
print(arr1)
print(arc)
