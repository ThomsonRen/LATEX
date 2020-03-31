# -*- coding: cp936 -*-
import numpy as np
import matplotlib.pyplot as plt
import copy
from math import *
from random import *

x = np.linspace(0.0, 4.0)
y = np.cos(0 * x) - np.cos(3 * x) * np.exp(-x)

plt.subplot(1, 1, 1)
plt.plot(x, y, '-')    

def F(x): return 1.-cos(3.*x)*exp(-x)

def drawline(k, x, c, l):
    Y = np.linspace(0, F(x))
    X = [x] * len(Y) 
    if (k == 0): plt.plot(X, Y, '-', linewidth=2.5, color = c, label = l)
    else: plt.plot(X, Y, '-', linewidth=2.5, color = c)
    
N = 3 
x = [uniform(0, 4) for i in range(N)] 

for i in range(N): drawline(i, x[i], "red", "beginning")

V = [0 for i in range(N)] 
p = copy.copy(x) 
pg = -1 
for i in range(N):
    if (pg < 0 or F(pg) < F(x[i])): pg = x[i]

c1 = 2
c2 = 2 
vmax = 2
for ti in range(100): 
    for i in range(N):
        V[i] += c1*random()*(p[i]-x[i])+c2*random()*(pg-x[i])
        if (V[i]<0 and V[i]<-vmax): V[i] = -vmax;
        if (V[i]>0 and V[i]>vmax):  V[i] = vmax;
        x[i] += V[i]
        if (x[i]<0): x[i]=0
        if (x[i]>4): x[i]=4
        if (F(x[i])>F(p[i])): p[i]=x[i]
        if (F(x[i])>F(pg)): pg=x[i]
    if ti == 9:
        for i in range(N): drawline(i, p[i], "blue", "the 10th time")
    if ti == 99:
        for i in range(N): drawline(i, p[i], "green", "the 100th time")

plt.legend(loc='upper right')
plt.show()























