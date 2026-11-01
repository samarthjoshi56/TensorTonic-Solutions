import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    m = len(A)
    n = len(A[0])
    
    result = [[A[i][j] for i in range(m)] for j in range(n)]
    
    return np.array(result)