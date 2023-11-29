import numpy as np

a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
b = np.array([[10, 20, 30, 40, 50]])
print(a.shape, b.shape)
print(a + b)
print(f"A Soma acumulada é {((a + b).cumsum())}")