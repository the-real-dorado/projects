import matplotlib.pyplot as plt
import numpy as np
import random

a = 1
r = a/(2*np.sqrt(3))
R = a/(  np.sqrt(3))
P1 = [0,R]
P2 = [ np.sqrt(R**2-r**2),-r]
P3 = [-np.sqrt(R**2-r**2),-r]

n = 60*10*20 # number of points
X = list(map(lambda a,b:(a+b)/2,P1,P2))
plt.figure(figsize=(5,5))
plt.xlim(-np.sqrt(R**2-r**2)-0.05,np.sqrt(R**2-r**2)+0.05)
plt.ylim(-r-0.05,R+0.05)

plt.axis('off')
for i in range(0,n): # chaos game
    X = list(map(lambda a,b:(a+b)/2,X,random.choice([P1,P2,P3])))
    plt.plot(X[0],X[1],'k.',ms=1)
    if i%20==0:
        plt.savefig(f'triangle/triangle-{(i//20)+1}.png',dpi=200)