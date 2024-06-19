#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

y = np.array([55, 10, 20, 15])
myLabels = np.array(["Playing factorio", "Studying", "Doing dishes", "Being productive"])
explose = [0.1, 0.1, 0.2, 0.15]

plt.pie(y, labels = myLabels, explode = explose) 
plt.title("What jack does with his time")
#Two  lines to make our compiler able to draw:
plt.savefig("figure.png")
sys.stdout.flush()

