import numpy as np
arr1 = np.array([[3,2,5],[1,7,4],[8,6,9]])
# print(arr1)
print('amax() function')
print("Maximum element : ", np.amax(arr1))
print("ColumnWise: ",np.amax(arr1,axis=0))
print("RowWise: ", np.amax(arr1,axis=1))

print('amin() function')
print("Minimum element : ", np.amin(arr1))
print("ColumnWise: ",np.amin(arr1,axis=0))
print("RowWise: ", np.amin(arr1,axis=1))

print('average() function')#mean and average returns the same value
print("Average element : ", np.average(arr1))
print("ColumnWise: ",np.average(arr1,axis=0))
print("RowWise: ", np.average(arr1,axis=1))

print('median() function')
print("Median element : ", np.median(arr1))
print("ColumnWise: ",np.median(arr1,axis=0))
print("RowWise: ", np.median(arr1,axis=1))

print('var() function')
print("Variance : ", np.var(arr1))
print("ColumnWise: ",np.var(arr1,axis=0))
print("RowWise: ", np.var(arr1,axis=1))

print('std() function')
print("Standard Deviation : ", np.std(arr1))
print("ColumnWise: ",np.std(arr1,axis=0))
print("RowWise: ", np.std(arr1,axis=1))
