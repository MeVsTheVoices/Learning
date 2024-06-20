import numpy as np
from scipy.sparse import csr_matrix, csc_matrix

arr = np.array([0,0,0,0,1,1,1,1,2,2,2,2,4,6,6,8])

print(csr_matrix(arr))

arr = np.array([[0,0,0],[0,0,1],[1,0,2]])

print(csr_matrix(arr).data)
print(csr_matrix(arr).count_nonzero())
print(csr_matrix(arr).sum_duplicates())
