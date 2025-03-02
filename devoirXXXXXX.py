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

xn1 = pointfixe(g, -1.5, 50, 10**-7)
xn2 = pointfixe(g, 1.5, 50, 10**-7)

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
    Enplus1surEn = np.array([])
    for i, x in enumerate(colonne_En):
        if i < (len(colonne_En) - 1):
            Enplus1surEn = np.append(Enplus1surEn, colonne_En[i+1]/x**2)
    return Enplus1surEn


plt.semilogy(range(0, len(En_array(xn1, -1))), En_array(xn1, -1), label = 'racine 1')
plt.semilogy(range(0, len(En_array(xn2, 1))), En_array(xn2, 1), label = 'racine 2')
plt.xlabel('n')
plt.ylabel('En')
plt.title("En en fonction de n")
plt.legend()
plt.show()


plt.plot(range(0, len(Enplus1surEn_array(En_array(xn1, -1)))),
          Enplus1surEn_array(En_array(xn1, -1)), label = 'racine 1')
plt.plot(range(0, len(Enplus1surEn_array(En_array(xn2, 1)))),
          Enplus1surEn_array(En_array(xn2, 1)), label = 'racine 2')
plt.xlabel('n')
plt.ylabel('(En+1)/En')
plt.title("(En+1)/En en fonction de n")
plt.legend()
plt.show()


'''QUESTION 2'''


def g2(x):
    return x - (x**3 - x**2 - x + 1)/(3 * x**2 -2 * x -1)

xn1 = pointfixe(g2, -1.5, 50, 10**-7)
xn2 = pointfixe(g2, 1.5, 50, 10**-7)

plt.semilogy(range(0, len(En_array(xn1, -1))), En_array(xn1, -1), label = 'racine 1')
plt.semilogy(range(0, len(En_array(xn2, 1))), En_array(xn2, 1), label = 'racine 2')
plt.xlabel('n')
plt.ylabel('En')
plt.title("En en fonction de n (Newton)")
plt.legend()
plt.show()

plt.plot(range(0, len(Enplus1surEn2_array(En_array(xn1, -1)))),
          Enplus1surEn2_array(En_array(xn1, -1)))
plt.xlabel('n')
plt.ylabel('(En+1)/En^2')
plt.title("(En+1)/En^2 en fonction de n pour r_1 (Newton) ")
plt.legend()
plt.show()

print(xn2)
print(En_array(xn2, 1))
print(Enplus1surEn_array(En_array(xn2, 1)))
plt.plot(range(0, len(Enplus1surEn_array(En_array(xn2, 1)))),
          Enplus1surEn_array(En_array(xn2, 1)))
plt.xlabel('n')
plt.ylabel('(En+1)/En')
plt.title("(En+1)/En en fonction de n pour r_2 (Newton)")
plt.legend()
plt.show()

'''QUESTION 3'''

'''QUESTION 4'''

def fsecante(x_n, x_nm1):
    return x_n - (((x_n**3 - x_n**2 - x_n + 1)*(x_n - x_nm1))/(x_n**3 - x_n**2 - x_n + 1 - x_nm1**3 + x_nm1**2 + x_nm1 -1))