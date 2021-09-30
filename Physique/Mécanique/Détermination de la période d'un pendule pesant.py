import math as m
import numpy as np
import matplotlib.pyplot as plt

m1 = 100*(10**-3) #100g
g = 9.81
l = 50*(10**-3) #50cm
a = 25*(10**-3) #25cm, le milieu de la tige de 50cm
J = (1/3)*m1*(l**2)

theta0 = np.linspace(0.1, m.pi, 1000)
periode = []
debut = 0

def f(x, theta0):
    return 1/(m.sqrt(2*m1*g*a*(m.cos(x)-m.cos(theta0))/J))

def integral(f, a, b, n):
    h = (b-a)/n
    res = 0
    for i in range(n):
        res += h*f(a+i*h, b) #b=théta0
    return res

periode = []

for elt in theta0:
    periode.append(4*integral(f, debut, elt, 1000))
    print(elt)

plt.plot(theta0, periode)
plt.xlabel("Théta 0 (rad)")
plt.ylabel("Période (s)")
plt.title("Période d'un pendule pesant en fonction de théta 0")
plt.grid()
plt.show()
