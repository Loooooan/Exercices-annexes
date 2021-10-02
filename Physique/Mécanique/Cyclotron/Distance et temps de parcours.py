import math as m

m1 = 1.67*10**-(27)
n = 0
U = 5000
e = 1.6*10**(-19)
B = 0.8
R = 0.3

T = m.pi*m1/(e*B)
vitesse_max = R*e*B/m1

distance_parcourue = 0
temps_de_parcours_methode1 = 0

def vitesse(n):
    return m.sqrt(2*n*e*U/m1)

while m.sqrt(2*n*e*U/m1) < vitesse_max:
    distance_parcourue += vitesse(n)*T
    temps_de_parcours_methode1 += T
    n += 1

temps_de_parcours_methode2 = n*T

print(n)
print(distance_parcourue)
print(temps_de_parcours_methode1)
print(temps_de_parcours_methode2)
