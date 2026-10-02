import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    x_arr = np.asarray(x, dtype=float)
    sig = 1 / (1 + np.exp(-x_arr))
    
    if np.isscalar(x):
        return float(sig)
    return sig