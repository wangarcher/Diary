import numpy as np

t1 = t2 = t3 = np.pi/3
l1 = l2 = l3 = 10
#x = float(input("final x position:"))
#y = float(input("final y position:"))
x = 10
y = 20
t = np.array([x, y])
tv = np.array([t1, t2, t3])
n = 4
while(n > 0):
    X = l1*np.cos(tv[0])+l2*np.cos(tv[0]+tv[1])+l3*np.cos(tv[0]+tv[1]+tv[2])
    Y = l1*np.sin(tv[0])+l2*np.sin(tv[0]+tv[1])+l3*np.sin(tv[0]+tv[1]+tv[2])
    T = np.array([X, Y])
    J = np.array([[-l1*np.sin(tv[0])-l2*np.sin(tv[0]+tv[1])-l3*np.sin(tv[0]+tv[1]+tv[2]), -l2*np.sin(tv[0]+tv[1])-l3*np.sin(tv[0]+tv[1]+tv[2]), -l3*np.sin(tv[0]+tv[1]+tv[2])],
                  [l1*np.cos(tv[0])+l2*np.cos(tv[0]+tv[1])+l3*np.cos(tv[0]+tv[1]+tv[2]), l2*np.cos(tv[0]+tv[1])+l3*np.cos(tv[0]+tv[1]+tv[2]), l3*np.cos(tv[0]+tv[1]+tv[2])]
                  ])
    Ji = np.linalg.pinv(J)
    Terr = t - T
    tv = tv + Ji.dot(Terr)
    n = n - 1
print(tv)