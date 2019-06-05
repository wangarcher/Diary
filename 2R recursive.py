import numpy as np

t1 = np.pi/3
t2 = -np.pi/3
x = y = 10
t = np.array([x, y])
l1 = l2 = 10
#x = float(input("final x position:"))
#y = float(input("final y position:"))
tv = np.array([t1, t2])
n = 4
while(n > 0):
    X = l1*np.cos(tv[0])+l2*np.cos(tv[0]+tv[1])
    Y = l1*np.sin(tv[0])+l2*np.sin(tv[0]+tv[1])
    T = np.array([X, Y])
    J = np.array([[-l1*np.sin(tv[0])-l2*np.sin(tv[0]+tv[1]), -l2*np.sin(tv[0]+tv[1])],
                  [l1*np.cos(tv[0])+l2*np.cos(tv[0]+tv[1]), l2*np.cos(tv[0]+tv[1])]
                  ])
    Ji = np.linalg.inv(J)
    Terr = t - T
    print(Terr)
    tv = tv + Ji.dot(Terr.T)
    n = n-1
print(tv)