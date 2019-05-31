import numpy as np

def keyin():
    a = float(input("angle:"))
    b = float(input("length:"))
    return a, b

def calculate(t, l):
    M = np.array([[np.cos(t), -1*np.sin(t), 0, l*np.cos(t)],
              [np.sin(t), np.cos(t), 0, l*np.sin(t)],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])
    return M


B = np.identity(4)
n = int(input("joint number:"))

while(n > 0):
    x, y = keyin()
    A = calculate(x, y)
    B = B.dot(A)
    n = n - 1
print (B)



