import math as m

theta0 = 1
m = 100*(10**-3) #100g
g = 9.81
l = 50*(10**-3) #50cm
a = 25*(10**-3) #25cm, le milieu de la tige de 50cm
J = (1/3)*m*(l**2)

debut = 0
fin = theta0

def f(x):
    return 1/(m.sqrt(2*m*g*a*(m.cos(x)-m.cos(theta0))/J))

def integral(f, a, b, n):
    h = (b-a)/n
    res = 0
    for i in range(n):
        res += h*f(a+i*h)
    return res

valeur_integral = integral(f, debut, fin, 1000)
periode = 4*valeur_integral

print(valeur_integral)
print(periode)

#Erreur:
#line 14, in f
#    return 1/(m.sqrt(2*m*g*a*(m.cos(x)-m.cos(theta0))/J))
#AttributeError: 'float' object has no attribute 'sqrt'
