import numpy as np
arr1 = np.array([4,8,9,5,14,36])
arr2 = np.array([2,8,21,8,14,52])
arr3 = (arr1 == arr2)
print(arr3)
if(np.any(arr3)):
    print("Some values matches")
else:
    print('No same prices')
if(np.all(arr3)):
    print("All values matches")
else:
    print('No identical prices')


arr4 = np.where(arr1%2==0,arr1,0)#if true places the elements of arr1 otherwise 0
print(arr4)