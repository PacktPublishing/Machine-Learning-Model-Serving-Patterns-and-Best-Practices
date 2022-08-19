import numpy as np
import sys
X = [
    [1.5, 6.5, 7.5, 8.5],
    [1.5, 6.5, 7.5, 8.5],
    [1.5, 6.5, 7.5, 8.5],
    [1.5, 6.5, 7.5, 8.5]
]
A = np.array(X, dtype='float64')
B = A.astype(np.uint8)
print(A)
print(sys.getsizeof(A))
print(B)
print(sys.getsizeof(B))
