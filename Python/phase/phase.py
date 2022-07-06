import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# solve_ivp input function (no 't')
def dSdt(t, S):
    T, Td = S
    return [Td,
            -0.7*Td-np.sin(T)]

# phase space
div = 100
X, Y = np.meshgrid(np.linspace(-np.pi*2, np.pi*2, div),
                   np.linspace(-3, 3, div))
U, V = np.zeros((div,div)), np.zeros((div,div))
for i in range(div):
    for j in range(div):
        U[i, j], V[i, j] = dSdt(None, [X[i, j],Y[i, j]]) #None for no t in dSdt
M = np.sqrt(U**2 + V**2)

# set up plot
# start = []
plt.streamplot(X,Y,U,V,2,M/M.max())
# plt.quiver(X,Y,U,V)

# plt.xlabel("f")
# plt.ylabel("f '")
# plt.axhline(0,color='k',lw=0.2)
# plt.axvline(0,color='k',lw=0.2)
# plt.grid()
# plt.savefig("phase.png",dpi=300,facecolor="w")
plt.show()
