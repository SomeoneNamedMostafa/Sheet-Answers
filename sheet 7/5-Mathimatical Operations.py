import numpy as np

a = np.arange(100).reshape(-1, 10)  

print("\n a + 1: \n", a+1)  #Q14
print("\n a - 1: \n", a-1)
print("\n a * 2: \n", a*2)
print("\n a / 2: \n", a/2)
print("\n a ** 2: \n", a**2)

print("\n a > 50: \n", a>50)  #Q15
print("\n a < 50: \n", a<50)
print("\n a >= 50: \n", a>=50)

a = np.array([1, 2, 3])  #Q16
b = np.array([4, 5, 6])
print("\n a + b: \n", a+b)
print("\n a - b: \n", a-b)
print("\n a * b: \n", a*b)
print("\n a / b: \n", a/b)

print("\n a > b: \n", a>b)  #Q17
print("\n a < b: \n", a<b)
print("\n a >= b: \n", a>=b)