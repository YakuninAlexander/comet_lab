import numpy as np
import matplotlib.pyplot as plt

G=6.674184*(10**-11)
M=1.9891*(10**16)
x0 = 100
h = 0.001
time=np.arange(0,10,h)

def func(t, r):
    x = r[0]
    z = r[1]
    y = r[2]
    z1 = r[3]

    R = np.sqrt((x**2)+(y**2))
    fx = z
    fz = -(G*M)*(x/R**3)
    fy = z1
    fz1 = -(G*M)*(y/R**3)

    return np.array([fx, fz, fy, fz1], float)

def r_init(a, v0):
    y0 = 0
    fx0 = v0*np.cos(np.radians(a))
    fy0 = v0*np.sin(np.radians(a))
    return np.array([x0, fx0, y0, fy0], float)

def runge_kutt(t, r):
    k1 = func(t, r)
    prom = [None] * 4
    for i in range(len(r)):
        prom[i] = r[i] + k1[i]*(h/2.0)
    k2 = func(t + h/2.0, prom)
    for i in range(len(r)):
        prom[i] = r[i] + k2[i]*(h/2.0)
    k3 = func(t+h/2.0, prom)
    for i in range(len(r)):
        prom[i] = r[i] + k3[i]*h
    k4 = func(t+h, prom)
    for i in range(len(r)):
        r[i] = r[i] + (h/6.0)*(k1[i] + 2.0*k2[i] + 2.0*k3[i] + k4[i])
    return r

def pos(a, v0):
    xpositions=[]
    ypositions=[]
    val_x=[]
    val_y=[]
    r = r_init(a, v0)
    for t in time:
        r = runge_kutt(t, r)
        xpositions.append(r[0])
        val_x.append(r[1])
        ypositions.append(r[2])
        val_y.append(r[3])
    return xpositions, ypositions, val_x, val_y

x_pos, y_pos, val_x, val_y = pos(30, 100.2)
fig = plt.figure()
graf = fig.add_subplot(111)
graf.plot(x_pos, y_pos)
plt.show()



