import numpy as np

def secante(f, x0, x1, nmax, tolr):
    iterations = np.array([x0, x1])
    iterations = np.append(iterations,f(x0))
    iterations = np.append(iterations,f(x1))
    n = 2
    eps = np.finfo(np.float64).eps
    err_rel = np.abs(iterations[n]-iterations[n-1])/(np.abs(iterations[n])+eps)
    while (err_rel >= tolr and n < nmax):
        iterations = np.append(iterations,f(iterations[n], iterations[n-1]))
        err_rel = np.abs(iterations[n+1]-iterations[n])/(np.abs(iterations[n+1])+eps)
        n += 1
    return iterations