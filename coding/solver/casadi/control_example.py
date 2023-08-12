import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

from casadi import *

w = []
g = []
J = 0
Np = 50
Ns = 2
Nc = 1
dt = 0.1

x = SX.sym('x', (Ns, Np+1))
u = SX.sym('u', (Nc, Np))

xk = SX.sym('xk', Ns) # x, v
uk = SX.sym('uk', Nc) # a

# given loss and dynamics
xkdot = vertcat(xk[1], uk[0])
L = (xk[0]-15)**2 + xk[1]**2 + uk[0]**2

F = Function('F', [xk, uk], [xkdot, L], ['xk', 'uk'], ['xdot', 'L'])


for idx in range(Np):
    Fk = F(xk=x[:, idx], uk=u[:, idx])
    w += [x[:, idx], u[:, idx]]
    g += [Fk['xdot']*dt + x[:, idx] - x[:, idx+1]]
    J += Fk['L']

w += [x[:, Np]]
g += [x[:,0]]

prob = {'f': J, 'x': vertcat(*w), 'g': vertcat(*g)}
nlp_opts = {"verbose": False}
solver = nlpsol('solver', 'ipopt', prob, nlp_opts);
r = solver(lbg=0, ubg=0)

results = r['x']
Nsc = Ns + Nc
r_x = results[np.arange(Np+1)*Nsc + 0]
r_v = results[np.arange(Np+1)*Nsc + 1]
r_a = results[np.arange(Np)*Nsc + 2]

plt.figure()
plt.plot(r_x, label='x')
plt.plot(r_v, label='v')
plt.plot(r_a, label='a')
plt.legend()
plt.show()
