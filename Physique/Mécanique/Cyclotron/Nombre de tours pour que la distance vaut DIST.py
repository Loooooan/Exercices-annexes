import math as m

def DISTPARCOURUE(dist, v0, m1, e, B, U):
    T = m.pi*m1/(e*B)
    n = 0
    distance_parcourue = 0
    while distance_parcourue < dist:
        distance_parcourue += m.sqrt(2*n*e*U/m1 + v0**2)*T
        n += 1
    return n
