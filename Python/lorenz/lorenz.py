import numpy as np
import pandas as pd
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import plotly.express as px

r = 28.0
s = 10.0
b = 8.0 / 3.0

def dSdt(S, t):
    x,y,z = S
    return s*(y-x), x*(r-z)-y, x*y-b*z

S = ((1.0,1.0,1.0),
     (1.0,1.0,2.0),
     (1.0,1.0,3.0),
     (1.0,1.0,4.0))

c = 'tab:red','tab:orange','tab:cyan','tab:blue'

for T in np.arange(0.1,30,0.01):
    fig = plt.figure(figsize=(10,10))
    ax = plt.axes(projection='3d',proj_type = 'ortho')
    ax.set_facecolor('k')
    ax.set_axis_off()
    ax.set_xlim([-20,20])
    ax.set_ylim([-20,20])
    ax.set_zlim([0,50])
    ax.view_init(20,-45)
    plt.tight_layout()
    t = np.arange(0.0, T, 0.01)
    for i,v in enumerate(S):
        x,y,z = list(zip(*odeint(dSdt, v, t)))
        ax.plot(x,y,z,lw=0.6,color=c[i])
        ax.plot(x[-1],y[-1],z[-1],lw=0.6,color=c[i],marker='.')
    # plt.savefig(f'lorenz/{T*100:.0f}.png',facecolor='k',dpi=200)
    print(T)
    fig.clf()
    plt.close()