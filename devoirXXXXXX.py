import numpy as np
import matplotlib.pyplot as plt
from math import e

def f(x):
    return (x+1)(x-1)**2

def g(x):
    return x - f(x)/5