import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# governing equations
def dSdt(t, S):
    T, Td = S
    return [Td,
            -0.4*Td-np.sin(T)]

# solving differential equations
S0 = (np.pi/2,-3.7)
time = 30
step = 24
t = np.linspace(0,time,time*step)
print("solving")
sol = solve_ivp(dSdt, (0,t.max()), S0, method='BDF', dense_output=True)
T = sol.sol(t)[0]
Td = sol.sol(t)[1]

# phase space
div = 100
X, Y = np.meshgrid(np.linspace(-np.pi*3, np.pi*3, div),
                   np.linspace(-6, 6, div))
U, V = np.zeros((div,div)), np.zeros((div,div))
for i in range(div):
    for j in range(div):
        U[i, j], V[i, j] = dSdt(100, [X[i, j],Y[i, j]]) # None for no t in dSdt
M = np.sqrt(U**2 + V**2)
print("rendering phase space")
plt.streamplot(X,Y,U,V,2,2*M/M.max())
plt.xlim(-np.pi*3, np.pi*3, step)
plt.ylim(-6,6)
plt.xlabel(r"$\theta$")
plt.ylabel(r"$\omega$",rotation=0)
plt.axhline(0,color='k',lw=0.2)
plt.axvline(0,color='k',lw=0.2)
theta = np.arange(-3*np.pi, 3*np.pi+np.pi/2, step=np.pi)
plt.xticks(theta, ['$-3\pi$','$-2\pi$','$-\pi$','$0$','$\pi$','$2\pi$','$3\pi$',])
plt.grid()
plt.savefig("phase_render/phase.png",dpi=300,facecolor="w")
plt.show()
for i in range(t.size):
    plt.plot(T[0:i],Td[0:i],color='orange')
    plt.xlim(-np.pi*3, np.pi*3, step)
    plt.ylim(-6,6)
    plt.axis('off')
    plt.savefig("phase_render/phase{}.png".format(i+1),dpi=300,transparent=True)
    plt.show()
    plt.clf()

# simulation
print("rendering simulation")
for i in range(t.size):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot(np.sin(T[0:i]), -t[0:i], -np.cos(T[0:i]), label='parametric curve',clip_on=True)
    ax.plot([0,np.sin(T[i-1])],[-t[i-1],-t[i-1]],[0,-np.cos(T[i-1])], "k",lw=0.7)
    ax.plot(np.sin(T[i-1]), -t[i-1], -np.cos(T[i-1]),"o")
    ax.set_xlim([-1,1])
    ax.set_ylim([-i/step-2,-i/step+10])
    ax.set_zlim([-1,1])
    fig.tight_layout()
    ax.set_axis_off()
    # ax.view_init(azim=-90, elev=0)
    ax.set_box_aspect((1, 1, 1))
    plt.savefig("phase_render/sim{}.png".format(i+1),dpi=300,facecolor="w")
    plt.show()
    # plt.clf()

print("done")
