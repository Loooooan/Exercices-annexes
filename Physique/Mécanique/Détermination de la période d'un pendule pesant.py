import math as m
import numpy as np
import matplotlib.pyplot as plt

m1 = 100*(10**-3) #100g
g = 9.81
l = 50*(10**-3) #50cm
a = 25*(10**-3) #25cm, le milieu de la tige de 50cm
J = (1/3)*m1*(l**2)
T0 = (2*m.pi)*m.sqrt(J/(m1*g*a))

theta0 = np.linspace(0.1, m.pi, 1000)
periode = []
rapport = []
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
    T = 4*integral(f, debut, elt, 1000)
    periode.append(T)
    rapport.append(T/T0)

fig, axs = plt.subplots(2)
fig.suptitle("Etude de la période d'un pendule pesant")
axs[0].plot(theta0, periode)
axs[0].set(xlabel='Théta 0 (rad)', ylabel='Période (s)')
axs[1].plot(theta0, rapport)
axs[1].set(xlabel='Théta 0 (rad)', ylabel='Rapport T0/T')

plt.show()
