#!/usr/bin/env python3

# by vdelaluz@enesmorelia.unam.mx

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.mlab as mlab

bins = np.arange(1,100)

plt.title("Poll results for 1000 simulations")

y = norm.pdf( bins, 12.16, 0.07)
l = plt.plot(bins, y, linewidth=2)

y = norm.pdf( bins, 64.75, 0.1)
l = plt.plot(bins, y, linewidth=2)

y = norm.pdf( bins, 23.07, 0.9)
l = plt.plot(bins, y, linewidth=2)



plt.show()
