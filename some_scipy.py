from scipy import constants
from scipy.optimize import root, minimize
import matplotlib
import numpy as np
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def eqn(x):
    return np.cos(x)

myroot = root(eqn, -1)
myminima = minimize(eqn, -1, method='BFGS')
mymaxima = minimize(lambda x : -eqn(x), -1, method='BFGS')

print(myroot.x)

x = np.arange(-5, 5, 0.1)
plt.plot(x, eqn(x), label='cos(x)')
plt.plot(x, [eqn(myroot.x) for i in x], label='root')
plt.plot(x, [eqn(mymaxima.x) for i in x], label='minima')
plt.plot(x, [eqn(myminima.x) for i in x], label='maxima')
plt.legend()
plt.savefig("sin_graph.png")

