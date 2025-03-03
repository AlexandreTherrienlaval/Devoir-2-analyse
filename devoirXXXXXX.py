import numpy as np
import matplotlib.pyplot as plt
from math import e
from pointfixe import pointfixe
from secante import secante

def f(x):
    return (x+1)*(x-1)**2



'''QUESTION 1'''


def g(x):
    return x - f(x)/5

xn_1 = pointfixe(g, -1.5, 50, 10**-7)
xn_2 = pointfixe(g, 1.5, 50, 10**-7)

def En_array(colonne_xn, r):
    En = np.array([])
    for i, x in enumerate(colonne_xn):
        if i < (len(colonne_xn)):
            En = np.append(En, abs(x - r))
    return En

def Enplus1surEn_array(colonne_En):
    Enplus1surEn = np.array([])
    for i, x in enumerate(colonne_En):
        if i < (len(colonne_En) - 1):
            Enplus1surEn = np.append(Enplus1surEn, colonne_En[i+1]/x)
    return Enplus1surEn

def Enplus1surEn2_array(colonne_En):
    Enplus1surEn2 = np.array([])
    for i, x in enumerate(colonne_En):
        if i < (len(colonne_En) - 1):
            Enplus1surEn2 = np.append(Enplus1surEn2, colonne_En[i+1]/x**2)
    return Enplus1surEn2

plt.semilogy(range(0, len(En_array(xn_1, -1))), En_array(xn_1, -1), label = 'racine 1')
plt.semilogy(range(0, len(En_array(xn_2, 1))), En_array(xn_2, 1), label = 'racine 2')
plt.xlabel('n')
plt.ylabel('E_n')
plt.title("E_n en fonction de n")
plt.legend()
plt.show()

plt.plot(range(0, len(Enplus1surEn_array(En_array(xn_1, -1)))), Enplus1surEn_array(En_array(xn_1, -1)), label = 'racine 1')
plt.plot(range(0, len(Enplus1surEn_array(En_array(xn_2, 1)))), Enplus1surEn_array(En_array(xn_2, 1)), label = 'racine 2')
plt.xlabel('n')
plt.ylabel('(E_n+1)/E_n')
plt.title("(E_n+1)/E_n en fonction de n")
plt.legend()
plt.show()



'''QUESTION 2'''


def G1(x):
    return x - (x**3 - x**2 - x + 1) / (3*x**2 - 2*x - 1)

xn_1 = pointfixe(G1, -1.5, 50, 10**-7)
xn_2 = pointfixe(G1, 1.5, 50, 10**-7)

plt.semilogy(range(0, len(En_array(xn_1, -1))), En_array(xn_1, -1), label = 'racine 1')
plt.semilogy(range(0, len(En_array(xn_2, 1))), En_array(xn_2, 1), label = 'racine 2')
plt.xlabel('n')
plt.ylabel('E_n')
plt.title("E_n en fonction de n (Newton)")
plt.legend()
plt.show()

plt.plot(range(0, len(Enplus1surEn2_array(En_array(xn_1, -1)))), Enplus1surEn2_array(En_array(xn_1, -1)))
plt.xlabel('n')
plt.ylabel('(E_n+1)/E_n^2')
plt.title("(E_n+1)/E_n^2 en fonction de n pour r_1 (Newton)")
plt.show()

plt.plot(range(0, len(Enplus1surEn_array(En_array(xn_2, 1)))), Enplus1surEn_array(En_array(xn_2, 1)))
plt.xlabel('n')
plt.ylabel('(E_n+1)/E_n')
plt.title("(E_n+1)/E_n en fonction de n pour r_2 (Newton)")
plt.show()



'''QUESTION 3'''


def G2(x):
    return x - (g(x) - x)**2 / (g(g(x)) - 2*g(x) + x)

xn_1 = pointfixe(G2, -1.5, 50, 10**-7)

plt.plot(range(0, len(En_array(xn_1, -1))), En_array(xn_1, -1), label = 'racine 1')
plt.xlabel('n')
plt.ylabel('E_n')
plt.title("E_n en fonction de n pour r_1 (Steffensen)")
plt.show()

plt.plot(range(0, len(Enplus1surEn2_array(En_array(xn_1, -1)))), Enplus1surEn2_array(En_array(xn_1, -1)))
plt.xlabel('n')
plt.ylabel('(E_n+1)/E_n^2')
plt.title("(E_n+1)/E_n^2 en fonction de n pour r_1 (Steffensen)")
plt.show()



'''QUESTION 4'''

def fsecante(x_n, x_nm1):
    return x_n - (((x_n**3 - x_n**2 - x_n + 1)*(x_n - x_nm1))/(x_n**3 - x_n**2 - x_n + 1 - x_nm1**3 + x_nm1**2 + x_nm1 -1))