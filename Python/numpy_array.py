import numpy as np
a = np.array([[1, 2, 3, 5, 9], [2, 4, 3, 5, 11]])
b = np.column_stack(a)
c = np.corrcoef(a)
d = np.corrcoef(b)
print(a)
print(b)
print(c)
