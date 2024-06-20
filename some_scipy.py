from scipy import constants
from scipy.optimize import root
import matplotlib
import numpy as np
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def eqn(x):
    return np.cos(x)

myroot = root(eqn, -1)

print(myroot.x)

x = np.arange(-5, 5, 0.1)
plt.plot(x, eqn(x))
plt.plot(x, [eqn(myroot.x) for i in x])
plt.savefig("sin_graph.png")

