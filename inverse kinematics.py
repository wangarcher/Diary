import numpy as np
import math as m

L = [10, 10, 10]

def keyin():
    l = float(input("length:"))
    return l


#a = float(input("final angle:"))
#x = float(input("final x position:"))
#y = float(input("final y position:"))

a = 3
x = -8.65837027
y = 18.9188842

Sx = x - L[2]*np.cos(a)
Sy = y - L[2]*np.sin(a)
print(Sx, Sy)

S = Sx**2 + Sy**2

theta2 = -2*m.atan(m.sqrt(((L[0]+L[1])**2 - S)/(S - (L[0]-L[1])**2)))
D = L[0] + L[1]*np.cos(theta2)

A = np.array([[D, -L[1]*np.sin(theta2)],
              [L[1]*np.sin(theta2), D]])
b = np.array([Sx, Sy]).T
r = np.linalg.solve(A, b)
print(r)
theta1 = m.atan(r[1]/r[0])
theta3 = a + theta1 + theta2

print(theta1, theta2, theta3)

