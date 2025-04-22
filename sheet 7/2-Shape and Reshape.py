import numpy as np

arr_2D = np.arange(1, 10).reshape(3, 3)  #Q6
print(arr_2D)

arr_1D = arr_2D.flatten()  #Q7
print(arr_1D)

arr2 = np.arange(100)  #Q8
arr3 = arr2.reshape(4, -1)  
print(arr3)
print(arr3.shape)