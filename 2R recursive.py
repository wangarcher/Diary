import numpy as np

t1 = np.pi/3
t2 = -np.pi/3
x = y = 10
position = np.array([x, y])
l1 = l2 = 10
#x = float(input("final x position:"))
#y = float(input("final y position:"))
calc_theta = np.array([t1, t2])
n = 4
while(n > 0):
    X = l1*np.cos(calc_theta[0])+l2*np.cos(calc_theta[0]+calc_theta[1])
    Y = l1*np.sin(calc_theta[0])+l2*np.sin(calc_theta[0]+calc_theta[1])
    T = np.array([X, Y])
    J = np.array([[-l1*np.sin(calc_theta[0])-l2*np.sin(calc_theta[0]+calc_theta[1]), -l2*np.sin(calc_theta[0]+calc_theta[1])],
                  [l1*np.cos(calc_theta[0])+l2*np.cos(calc_theta[0]+calc_theta[1]), l2*np.cos(calc_theta[0]+calc_theta[1])]
                  ])
    Ji = np.linalg.inv(J)
    Terr = position - T
    calc_theta = calc_theta + Ji.dot(Terr.T)
    n = n-1
print(calc_theta)

