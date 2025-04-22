import numpy as np

a = np.arange(100).reshape(-1, 10)  #Q9
b = a[9][2]
print(b)

third_row= a[2,:]  #Q10
print(third_row)

fourth_clmn = a[:,3]  #Q11
print(fourth_clmn)