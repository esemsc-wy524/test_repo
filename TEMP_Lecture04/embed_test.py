import numpy as np
import matplotlib.pyplot as plt

Nx = 1000
x = np.linspace(-np.pi,np.pi,Nx)

def eval_fc(x,N):
    f = np.pi**2/3
    for i in range(1,N+1):
        f += 4*(-1)**i/N**2*np.cos(i*x)
    return f

y1 = eval_fc(x,1)
y2 = eval_fc(x,2)
y3 = eval_fc(x,5)
y4 = eval_fc(x,10)
y5 = eval_fc(x,100)

fig=plt.figure(figsize=(12,8), dpi= 60, facecolor='w', edgecolor='k')
plt.plot(x, y1, label = "$N=1$")
plt.plot(x, y2, label = "$N=2$")
plt.plot(x, y3, label = "$N=5$")
plt.plot(x, y4, label = "$N=10$")
plt.plot(x, y5, label = "$N=100$")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim((-1.0,11.5))
plt.legend()
plt.show()