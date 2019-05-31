import numpy as np
import math as m

L = [10, 10, 10] #length of the shaft

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
print(Sx, Sy)  #the position of the secondary joint

S = Sx**2 + Sy**2

theta2 = 2*m.atan(m.sqrt(((L[0]+L[1])**2 - S)/(S - (L[0]-L[1])**2)))
D = L[0] + L[1]*np.cos(theta2)

beta = m.acos((S + L[0]**2 -L[1]**2)/(2*L[0]*m.sqrt(S)))
alpha = m.atan2(Sy, Sx)
theta11 = alpha - beta
theta12 = alpha + beta
theta31 = a - theta11 - theta2
theta32 = a - theta12 - theta2
print(theta11, theta2, theta31 )
print(theta12, theta2, theta32 )

