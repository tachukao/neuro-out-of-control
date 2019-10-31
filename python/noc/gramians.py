from scipy.linalg import solve_lyapunov
import numpy as np
def obsv(a,c=None):
    if c is None:
        n = np.shape(a)[0]
        return solve_lyapunov(a.T,-np.eye(n))
    else:
        return solve_lyapunov(a.T,-c.T.dot(c))

def ctrl(a,b=None):
    if b is None:
        n = np.shape(a)[0]
        return solve_lyapunov(a,-np.eye(n))
    else:
        return solve_lyapunov(a,-b.dot(b.T)) 

