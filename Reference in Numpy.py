import numpy as np
arr1 = np.arange(1,11,1)
print(arr1)
print('Address of arr1 :',id(arr1))
arr_ref = arr1
print(arr_ref)#Reference create the array in same memory location as the original array
print('Address of arr_ref :',id(arr_ref))
arr1[3] = 500#Changes in any array(reference or original) reflect the change in both array
arr_ref[5] = 800
print('After change: ')
print(arr1)
print(arr_ref)
